from django.contrib import admin
from django.urls import path, include


app_name = 'boneadmin'

urlpatterns = [
    path('admin/', admin.site.urls),
    path('boneadmin/', include('Boneadmin.urls', namspace='boneadmin') )
]
