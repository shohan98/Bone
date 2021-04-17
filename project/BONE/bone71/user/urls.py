from django.contrib import admin
from django.urls import path, include

from rest_framework.routers import DefaultRouter

from .views import (user_index, user_video_player)

#from.views import (ContentDelete,)
app_name = 'boneuser'

router = DefaultRouter()

#router.register('contentdelete', ContentDelete, basename='contentdelete' )


urlpatterns = [
  path('', user_index, name='index'),
  path('video/<int:pk>/', user_video_player, name='video_player'),
  
  
#  path('boneuser/api/', include(router.urls)),
  
]
