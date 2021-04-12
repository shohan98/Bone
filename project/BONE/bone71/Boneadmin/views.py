from django.contrib.auth import login, authenticate
from django.shortcuts import render, redirect
from django.contrib import messages
from rest_framework.response import Response
from rest_framework.viewsets import ViewSet
from .forms import AdminSignUpForm
from django.contrib.auth.forms import AuthenticationForm

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
        return Response({'ok':'ok'})


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
    context = { 'message':message}
    return render(request, 'reg.html', context)


def admin_login(request):
    if request.method=='POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None :
                login(request,user)
                return render(request, 'login.html',context={'form':AuthenticationForm(), 'message':'Success!!'})
            else:
                messages.error(request,"Invalid username or password")
        else:
                messages.error(request,"Invalid username or password")
    return render(request, 'login.html',context={'form':AuthenticationForm()})


def admin_dashboard(request):
    return render(request, 'dashboard.html')


def admin_bannerad(request):
    return render(request, 'banner_ad.html')


def admin_motionad(request):
    return render(request, 'motion_ad.html')




def admin_videoad(request):
    return render(request, 'video_ad.html')


def admin_video_category(request):
    return render(request, 'video_category.html')

def dashboard_base(request):
    return render(request, 'dashboard_base.html')

def admin_youtube(request):
    if request.method=='POST':
        pass
    else:
        videos = YoutubeContent.objects.all()
        videos = YoutubeContentSerializer(videos, many=True)
        
    return render(request, 'youtube.html')
