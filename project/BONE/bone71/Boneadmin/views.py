from django.contrib.auth import login, authenticate
from django.shortcuts import render, redirect
from django.contrib import messages
from rest_framework.response import Response
from rest_framework.viewsets import ViewSet
from .forms import AdminSignUpForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from .decorators import admin_required
from django.conf import settings

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
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            print(user.is_admin)
            if user is not None:
                if user.is_admin:
                    login(request, user)
                    return redirect('boneadmin:dashboard')
                else:
                    return render(request, 'login.html', context={'form': AuthenticationForm(), 'message': 'This user is not an Admin!!'})
            else:
                messages.error(request, "Invalid username or password")
        else:
            messages.error(request, "Invalid username or password")
    return render(request, 'login.html', context={'form': AuthenticationForm()})

@login_required
@admin_required
def admin_dashboard(request):
    context = {'dashboard':'active'}
    return render(request, 'dashboard.html', context)

@login_required
@admin_required
def admin_bannerad(request):
    data=[]
    if request.method == 'POST':
        pass
    else:
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
    context = {'bannerad':'active', 'data':data}
    return render(request, 'banner_ad.html', context)

@login_required
@admin_required
def admin_motionad(request):
    data=[]
    if request.method == 'POST':
        pass
    else:
        videos = VerticalBannerAd.objects.all()
#        videos = YoutubeContentSerializer(videos, many=True)
        Vbanner_list = []
        for i in videos:
            Vbanner_list.append({
                        'id': i.id,
                        'banner_name': i.banner_name,
                        'banner': settings.MEDIA_URL+str(i.banner),
                        'postion': i.position,
                        'status': i.status
                    })
        data = Vbanner_list
    context = {'motionad':'active', 'data':data}
    return render(request, 'motion_ad.html', context)

@login_required
@admin_required
def admin_videoad(request):
    context = {'videoad':'active'}
    return render(request, 'video_ad.html', context)

@login_required
@admin_required
def admin_video_category(request):
    data=[]
    if request.method == 'POST':
        pass
    else:
        videos = VerticalBannerAd.objects.all()
#        videos = YoutubeContentSerializer(videos, many=True)
        Videoad_list = []
        for i in videos:
            Videoad_list.append({
                        'id': i.id,
                        'banner_name': i.video_name,
                        'banner': settings.MEDIA_URL+str(i.banner),
                        'toatal_watch': i.total_watch,
                        'status': i.status
                    })
        data = Videoad_list
    context = {'video_category':'active', 'data':data}
    return render(request, 'video_category.html', context)

@login_required
@admin_required
def dashboard_base(request):
    
    return render(request, 'dashboard_base.html')

@login_required
@admin_required
def admin_youtube(request):
    data=[]
    if request.method == 'POST':
        pass
    else:
        videos = YoutubeContent.objects.all()
#        videos = YoutubeContentSerializer(videos, many=True)
        video_list = []
        for i in videos:
            video_list.append({
                        'id': i.id,
                        'content_name': i.content_name,
                        'content_link': i.content_link,
                        'category': i.category.category_name,
                        'content_poster': settings.MEDIA_URL+str(i.content_poster)
                    })
        data = video_list
#        for i in videos.data:
            
    context = {'youtube':'active', 'data':data}
    return render(request, 'youtube.html', context)
