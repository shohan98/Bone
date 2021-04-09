from django.contrib import admin
from django.urls import path, include

from .views import signup, test
from rest_framework.routers import DefaultRouter
app_name = 'boneadmin'

router = DefaultRouter()

router.register('test', test, basename='test' )

urlpatterns = [
  path('signup', signup, name='signup'),
  path('api/', include(router.urls))
]
