from django.contrib.auth import login, authenticate, logout
from django.shortcuts import render, redirect
from django.contrib import messages
from rest_framework.response import Response
from rest_framework.viewsets import ViewSet, GenericViewSet
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.conf import settings
from django.core.files.storage import FileSystemStorage

#from .forms import AdminSignUpForm
#from .decorators import admin_required


def user_index(request):
    context = {'index':'active'}
    return render(request, 'index.html', context)



def user_video_player(request):
    context = {'video_player':'active'}
    return render(request, 'video-player.html', context)