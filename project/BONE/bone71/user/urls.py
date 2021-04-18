from django.contrib import admin
from django.urls import path, include

from rest_framework.routers import DefaultRouter

from .views import (user_index, user_video_player,logout)
from .views import (test)

#from.views import (ContentDelete,)
app_name = 'boneuser'

router = DefaultRouter()

router.register('test', test, basename='test' )


urlpatterns = [
  path('', user_index, name='index'),
  path('video/<int:pk>/', user_video_player, name='video_player'),
  path('logout', logout, name='logout'),
  
  path('boneuser/api/', include(router.urls)),
  
]
