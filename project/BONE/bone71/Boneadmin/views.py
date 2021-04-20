from django.contrib.auth import login, authenticate, logout
from django.shortcuts import render, redirect
from django.contrib import messages
from rest_framework.response import Response
from rest_framework.viewsets import ViewSet, GenericViewSet
from .forms import AdminSignUpForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from .decorators import admin_required, active_required
from django.conf import settings
from django.core.files.storage import FileSystemStorage
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticated

from .models import (YoutubeContent, ContentCategory, ContentClickMonthlyReport,
                     VerticalAdWatchMonthlyReport, VerticalBannerAd,
                     HorizontalAdWatchMonthlyReport, HorizontalBannerAd,
                     VideoAd, VideoAdWatchMonthlyReport, User)

from .serializers import (YoutubeContentSerializer, ContentCategorySerializer,
                          ContentClickMonthlyReportSerializer,
                          VerticalAdWatchMonthlyReportSerializer,
                          VerticalBannerAdSerializer, VideoAdWatchMonthlyReportSerializer,
                          VideoAdSerializer, HorizontalAdWatchMonthlyReportSerializer,
                          HorizontalBannerAdSerializer)


class test(ViewSet):
    def list(self, request):
        return Response({'ok': 'ok'})


class ContentDelete(ViewSet):
    authentication_classes = [SessionAuthentication, BasicAuthentication]
    permission_classes = [IsAuthenticated]
    def post(self, request):
        c_id = request.POST.get('c_id')
#        try:
        data = YoutubeContent.objects.get(id=c_id)
        data.delete()
        message="Delete Successfully"
        status = 204
#        except:
#            status=404
#            message="Delete Failed"
        return Response({'message':message}, status)
    
    def list(self, request):
        return Response({'message':'Get method not allowed'}, 405)

class CategoryDelete(ViewSet):
    authentication_classes = [SessionAuthentication, BasicAuthentication]
    permission_classes = [IsAuthenticated]
    def post(self, request):
        c_id = request.POST.get('c_id')
#        try:
        data = ContentCategory.objects.get(id=c_id)
        data.delete()
        message="Delete Successfully"
        status = 204
#        except:
#            status=404
#            message="Delete Failed"
        return Response({'message':message}, status)
    
    def list(self, request):
        return Response({'message':'Get method not allowed'}, 405)

class youtubeVideoDelete(ViewSet):
    authentication_classes = [SessionAuthentication, BasicAuthentication]
    permission_classes = [IsAuthenticated]
    def post(self, request):
        c_id = request.POST.get('c_id')
#        try:
        data = YoutubeContent.objects.get(id=c_id)
        data.delete()
        message="Delete Successfully"
        status = 204
#        except:
#            status=404
#            message="Delete Failed"
        return Response({'message':message}, status)
    
    def list(self, request):
        return Response({'message':'Get method not allowed'}, 405)


class VideoAdDelete(ViewSet):
    authentication_classes = [SessionAuthentication, BasicAuthentication]
    permission_classes = [IsAuthenticated]
    def post(self, request):
        c_id = request.POST.get('c_id')
#        try:
        data = VideoAd.objects.get(id=c_id)
        data.delete()
        message="Delete Successfully"
        status = 204
#        except:
#            status=404
#            message="Delete Failed"
        return Response({'message':message}, status)
    
    def list(self, request):
        return Response({'message':'Get method not allowed'}, 405)


class MotionAdDelete(ViewSet):
    authentication_classes = [SessionAuthentication, BasicAuthentication]
    permission_classes = [IsAuthenticated]
    def post(self, request):
        c_id = request.POST.get('c_id')
#        try:
        data = VerticalBannerAd.objects.get(id=c_id)
        data.delete()
        message="Delete Successfully"
        status = 204
#        except:
#            status=404
#            message="Delete Failed"
        return Response({'message':message}, status)
    
    def list(self, request):
        return Response({'message':'Get method not allowed'}, 405)


class BannerAdDelete(ViewSet):
    authentication_classes = [SessionAuthentication, BasicAuthentication]
    permission_classes = [IsAuthenticated]
    def post(self, request):
        c_id = request.POST.get('c_id')
#        try:
        data = HorizontalBannerAd.objects.get(id=c_id)
        data.delete()
        message="Delete Successfully"
        status = 204
#        except:
#            status=404
#            message="Delete Failed"
        return Response({'message':message}, status)
    
    def list(self, request):
        return Response({'message':'Get method not allowed'}, 405)



def csrf_failure(request, reason=""):
    current_url = request.get_full_path()
    return redirect(current_url)


def signup(request):
    if request.method == 'POST':
        form = AdminSignUpForm(request.POST)
        if form.is_valid():
            form.save()
            #            username = form.cleaned_data.get('username')
            #            raw_password = form.cleaned_data.get('password1')
            #            user = authenticate(username=username, password=raw_password)
            #            login(request, user)
            message = 'Register Successfully'
        else:
            message = str(form.errors)
    else:
        message = 'Here is your registration form'
    context = {'message': message}
    return render(request, 'reg.html', context)


def admin_login(request):
    message=''
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            print(username, password)
            user = authenticate(username=username, password=password)
            if user is not None:
                if user.is_admin:
                    login(request, user)
                    return redirect('boneadmin:dashboard')
                else:
                    return render(request, 'login.html', context={'form': AuthenticationForm(), 'message': 'This user is not an Admin!!'})
            else:
                message="Invalid username or password"
        else:
            message="Invalid username or password"
    return render(request, 'login.html', context={'form': AuthenticationForm(), 'message':message})

@login_required
@admin_required
@active_required
def admin_dashboard(request):
    context = {'dashboard':'active'}
    return render(request, 'dashboard.html', context)

@login_required
@admin_required
@active_required
def admin_bannerad(request):
    data=[]
    message=''
    if request.method == 'POST':
        banner_name = request.POST.get('name')
        target_link = request.POST.get('link')
        file = request.FILES['banner']
        try:
            try:
                data = HorizontalBannerAd.objects.create(banner_name=banner_name, 
                                 target_link=target_link, banner=file)
                data.save()
                message = "Conent Uploaded Successfully."
            except:
                message = "File Uploaded Failed"
        except:
            message = "Please Select Valid Category"

# Load all other elements
    videos = HorizontalBannerAd.objects.all()
#        videos = YoutubeContentSerializer(videos, many=True)
    hbanner_list = []
    for i in videos:
        hbanner_list.append({
                    'id': i.id,
                    'banner_name': i.banner_name,
                    'banner': settings.MEDIA_URL+str(i.banner),
                    'postion': i.position,
                    'status': i.status
                })
    data = hbanner_list
    context = {'bannerad':'active', 'data':data, 'message':message}
    return render(request, 'banner_ad.html', context)

@login_required
@admin_required
@active_required
def admin_motionad(request):
    data=[]
    message=''
    if request.method == 'POST':
        banner_name = request.POST.get('name')
        target_link = request.POST.get('link')
        file = request.FILES['banner']
        try:
            try:
                data = VerticalBannerAd.objects.create(banner_name=banner_name, 
                                 target_link=target_link, banner=file)
                data.save()
                message = "Conent Uploaded Successfully."
            except:
                message = "File Uploaded Failed"
        except:
            message = "Please Select Valid Category"

# Load all other elements
    videos = VerticalBannerAd.objects.all()
#        videos = YoutubeContentSerializer(videos, many=True)
    hbanner_list = []
    for i in videos:
        hbanner_list.append({
                    'id': i.id,
                    'banner_name': i.banner_name,
                    'banner': settings.MEDIA_URL+str(i.banner),
                    'postion': i.position,
                    'status': i.status
                })
    data = hbanner_list
    context = {'bannerad':'active', 'data':data, 'message':message}
    return render(request, 'motion_ad.html', context)


@login_required
@admin_required
@active_required
def admin_videoad(request):
    data=[]
    message=''
    if request.method == 'POST':
        video_name = request.POST.get('name')
        file = request.FILES['video']
        try:
            try:
                data = VideoAd.objects.create(video_name=video_name, 
                                 video=file)
                data.save()
                message = "Conent Uploaded Successfully."
            except:
                message = "File Uploaded Failed"
        except:
            message = "Please Select Valid Category"

# Load all other elements
    videos = VideoAd.objects.all()
#        videos = YoutubeContentSerializer(videos, many=True)
    hbanner_list = []
    for i in videos:
        hbanner_list.append({
                    'id': i.id,
                    'video_name': i.video_name,
                    'video': settings.MEDIA_URL+str(i.video),
                    'status': i.status
                })
    data = hbanner_list
    context = {'bannerad':'active', 'data':data, 'message':message}
    return render(request, 'video_ad.html', context)

@login_required
@admin_required
@active_required
def admin_video_category(request):
    data=[]
    message=""
    if request.method == 'POST':
        video_category = request.POST.get('video_category')
        try:
            category = ContentCategory.objects.create(category_name=video_category)
            category.save()
            message="Video Category Create Successfully"
        except:
            message="Video Category Create Failed."
        
    videos = ContentCategory.objects.all()
#        videos = YoutubeContentSerializer(videos, many=True)
    Videoad_list = []
    for i in videos:
        Videoad_list.append({
                    'id': i.id,
                    'category_name': i.category_name
                })
    data = Videoad_list
    context = {'video_category':'active', 'data':data, 'message':message}
    return render(request, 'video_category.html', context)

@login_required
@admin_required
@active_required
def dashboard_base(request):
    
    return render(request, 'dashboard_base.html')

@login_required
@admin_required
@active_required
def admin_youtube(request):
    data=[]
    message=''
    if request.method == 'POST':
        content_name = request.POST.get('name')
        content_link = request.POST.get('link')
        category = request.POST.get('video_category')
        desc = request.POST.get('desc')
        file = request.FILES['poster']
        try:
            category = ContentCategory.objects.get(id=category)
            try:
                data = YoutubeContent.objects.create(content_name=content_name, 
                                 content_link=content_link, category=category,
                                 content_description=desc, content_poster=file)
                data.save()
                category.total_video+=1
                category.save()
                message = "Conent Uploaded Successfully."
            except:
                message = "File Uploaded Failed"
        except:
            message = "Please Select Valid Category"

# Load all other elements
            
    videos = YoutubeContent.objects.all().order_by('created_at').reverse()
    category = ContentCategory.objects.all().order_by('created_at').reverse()
#        videos = YoutubeContentSerializer(videos, many=True)
    video_list = []
    category_list = []
    for i in videos:
        video_list.append({
                    'id': i.id,
                    'content_name': i.content_name,
                    'content_link': i.content_link,
                    'category': i.category.category_name,
                    'content_poster': settings.MEDIA_URL+str(i.content_poster)
                })
    for i in category:
        category_list.append({
                    'id': i.id,
                    'category_name': i.category_name,
                })
    data = video_list
#        for i in videos.data:
            
    context = {'youtube':'active', 'data':data, 'message': message, 'category':category_list}
    return render(request, 'youtube.html', context)

@login_required
@admin_required
@active_required
def logout_view(request):
    logout(request)
    return redirect('boneadmin:login')