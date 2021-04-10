from django.contrib.auth import login, authenticate
from django.shortcuts import render, redirect
from rest_framework.response import Response
from rest_framework.viewsets import ViewSet
from .forms import SignUpForm

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


def signup(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        p = request.POST.get('password1')
        c_p = request.POST.get('password2')
        if p==c_p:
            user = User.objects.create(username=username, email=email, password=p,
                                       is_user=True)
            user.save()
            message = 'Success'
#        form = SignUpForm(request.POST)
#        if form.is_valid():
#            form.is_user=True
#            form.save()
#            username = form.cleaned_data.get('username')
#            raw_password = form.cleaned_data.get('password1')
#            user = authenticate(username=username, password=raw_password)
#            login(request, user)
#            message = 'Register Successfully'
    else:
        message = 'Here is your registration form'
    context = { 'message':message}
    return render(request, 'reg.html', context)


def admin_login(request):
    return render(request, 'login.html')


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

def admin_youtube(request):
    if request.method=='POST':
        pass
    else:
        videos = YoutubeContent.objects.all()
        videos = YoutubeContentSerializer(videos, many=True)
        
    return render(request, 'youtube.html')
