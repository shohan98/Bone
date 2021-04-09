from django.contrib.auth import login, authenticate
from django.shortcuts import render, redirect
from rest_framework.response import Response
from rest_framework.viewsets import ViewSet
from .forms import SignUpForm

class test(ViewSet):
    def list(self, request):
        return Response({'ok':'ok'})

def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.is_admin=True
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            message = 'Register Successfully'
    else:
        message = 'Here is your registration form'
        form = SignUpForm()
    context = {'form': form, 'message':message}
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
    return render(request, 'youtube.html')
