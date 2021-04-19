from django.contrib.auth import login, authenticate, logout
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.conf import settings
from django.core.files.storage import FileSystemStorage
from rest_framework.response import Response
from rest_framework.viewsets import ViewSet, GenericViewSet
from rest_framework.views import APIView
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticated

from Boneadmin.models import User, YoutubeContent, ContentCategory
from .models import BoneUser
from .forms import UserSignUpForm

#from .forms import AdminSignUpForm
from .decorators import active_required
from .decorators import user_required

class test(ViewSet):
    authentication_classes = [SessionAuthentication, BasicAuthentication]
    permission_classes = [IsAuthenticated]
    def list(self, request):
        return Response({'ok': 'ok'})

def csrf_failure(request, reason=""):
    current_url = request.get_full_path()
    return redirect(current_url)


class Signup(ViewSet):
    def post(self, request):
        form = UserSignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            message = 'Register Successfully'+str(user)+str(request.user)
        else:
            message = str(form.errors)
        return Response({'msg': message})



def user_index(request):
    message=''
    if request.method == 'POST':
        if request.POST.get('type')=='login':
            print('****************')
#            form = AuthenticationForm(data=request.POST)
#            if form.is_valid():
            password = request.POST.get('password')
            email = request.POST.get('email')
            u = User.objects.get(email=email)
            user = authenticate(username=u.username, password=password)
            if user is not None:
                if user.is_user :
                    if user.is_active:
                        login(request, user)
                        return redirect('boneuser:index')
                    else:
                        message='Inactive user account.'
                else:
                    message = 'You are not a valid user!!'
            else:
                message="Invalid username or password"+email+password+str(request.user)
#            else:
#                message="Form is invalid"
        elif request.POST.get('type')=='signup':    
            form = UserSignUpForm(request.POST)
            if form.is_valid():
                form.save()
                email = form.cleaned_data.get('email')
                raw_password = form.cleaned_data.get('password')
                user = authenticate(email=email, password=raw_password)
                login(request, user)
                message = 'Register Successfully'
            else:
                message = str(form.errors)
        
    try:    
        category = ContentCategory.objects.filter().order_by('total_video')[0]
        video = YoutubeContent.objects.filter(category=category.id).order_by('total_click')
        video_list=[]
        for i in video:
            video_list.append({
                        'title': i.content_name,
                        'id': i.id,
                        'poster': settings.MEDIA_URL+str(i.content_poster)
                    })
    except:
        pass
    context = {'form': AuthenticationForm(), 'index':'active', 'message': request.user}
    return render(request, 'index.html', context)

@login_required(login_url='/')
@active_required
#@user_required
def user_video_player(request, pk):
    try:
        video = YoutubeContent.objects.get(id=pk)
        categories = ContentCategory.objects.filter()
        
        # Same Category video list
        same_category_video = YoutubeContent.objects.filter(category=video.category.id).order_by('total_click')
        same_category_video_list=[]
        for i in same_category_video:
            same_category_video_list.append({
                        'title': i.content_name,
                        'id': i.id,
                        'poster': settings.MEDIA_URL+str(i.content_poster),
                        'link': i.content_link
                    })
        
        # Latest Video List
        latest_video = YoutubeContent.objects.filter().order_by('created_at').reverse()
        latest_video_list=[]
        for i in latest_video:
            latest_video_list.append({
                        'title': i.content_name,
                        'id': i.id,
                        'poster': settings.MEDIA_URL+str(i.content_poster),
                        'link': i.content_link
                    })
            if len(latest_video_list)>=10:
                break
    
        #Most watched video list
        most_watch_video = YoutubeContent.objects.filter().order_by('total_click').reverse()
        most_watch_video_list=[]
        for i in most_watch_video:
            most_watch_video_list.append({
                        'title': i.content_name,
                        'id': i.id,
                        'poster': settings.MEDIA_URL+str(i.content_poster),
                        'link': i.content_link
                    })
            if len(most_watch_video_list)>=10:
                break
        context = {'video_player':'active', 'categories':categories, 'c_len':len(categories),
               'youtube':video.content_link, 'title': video.content_name,
               'desc':video.content_description, 'views': video.total_click,
               'similar_video': same_category_video_list,
               'latest_video': latest_video_list,
               'most_watch_video': most_watch_video_list}
        
        return render(request, 'video-player.html', context)
    except:
        return render(request, '404.html')
    
def logout_view(request):
    logout(request)
    return redirect('boneuser:index')