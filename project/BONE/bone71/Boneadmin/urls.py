from django.contrib import admin
from django.urls import path, include

from rest_framework.routers import DefaultRouter

from .views import (signup, test, admin_login, admin_bannerad, admin_youtube,
                    admin_motionad, admin_video_category, admin_videoad,
                    admin_dashboard)

app_name = 'boneadmin'

router = DefaultRouter()

router.register('test', test, basename='test' )

urlpatterns = [
  path('signup', signup, name='signup'),
  path('login', admin_login, name='login'),
  path('dashboard', admin_dashboard, name='dashboard'),
  path('bannerad', admin_bannerad, name='bannerad'),
  path('youtube', admin_youtube, name='youtube'),
  path('motionad', admin_motionad, name='motionad'),
  path('video_category', admin_video_category, name='login'),
  path('videoad', admin_videoad, name='login'),
  
  
  path('api/', include(router.urls)),
  
]
