import json

from django.contrib.auth import login, authenticate, logout
from django.shortcuts import render, redirect
from django.contrib import messages
from rest_framework.response import Response
from rest_framework.viewsets import ViewSet, GenericViewSet
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.conf import settings
from django.http import HttpResponse
from django.db.models import Q
from django.core.paginator import Paginator

from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticated

from .forms import AdminSignUpForm
from .decorators import admin_required, active_required
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

def page_data(request, data,per_page_value):
    try:
        paginator = Paginator(data, per_page_value)  # Show 25 contacts per page
        page = request.GET.get('page')
        if not page:
            page = request.POST.get('page')    
        return paginator.get_page(page)
    except:
        return data

class ContentDelete(ViewSet):
    authentication_classes = [SessionAuthentication, BasicAuthentication]
    permission_classes = [IsAuthenticated]
    def post(self, request):
        c_id = request.POST.get('c_id')
#        try:
        data = YoutubeContent.objects.get(id=c_id)
        data.delete()
        message="Delete Successfully"
        status = 204
#        except:
#            status=404
#            message="Delete Failed"
        return Response({'message':message}, status)
    
    def list(self, request):
        return Response({'message':'Get method not allowed'}, 405)

class CategoryDelete(ViewSet):
    authentication_classes = [SessionAuthentication, BasicAuthentication]
    permission_classes = [IsAuthenticated]
    def post(self, request):
        c_id = request.POST.get('c_id')
#        try:
        data = ContentCategory.objects.get(id=c_id)
        data.delete()
        message="Delete Successfully"
        status = 204
#        except:
#            status=404
#            message="Delete Failed"
        return Response({'message':message}, status)
    
    def list(self, request):
        return Response({'message':'Get method not allowed'}, 405)

class youtubeVideoDelete(ViewSet):
    authentication_classes = [SessionAuthentication, BasicAuthentication]
    permission_classes = [IsAuthenticated]
    def post(self, request):
        c_id = request.POST.get('c_id')
#        try:
        data = YoutubeContent.objects.get(id=c_id)
        data.delete()
        message="Delete Successfully"
        status = 204
#        except:
#            status=404
#            message="Delete Failed"
        return Response({'message':message}, status)
    
    def list(self, request):
        return Response({'message':'Get method not allowed'}, 405)


class VideoAdDelete(ViewSet):
    authentication_classes = [SessionAuthentication, BasicAuthentication]
    permission_classes = [IsAuthenticated]
    def post(self, request):
        c_id = request.POST.get('c_id')
#        try:
        data = VideoAd.objects.get(id=c_id)
        data.delete()
        message="Delete Successfully"
        status = 204
#        except:
#            status=404
#            message="Delete Failed"
        return Response({'message':message}, status)
    
    def list(self, request):
        return Response({'message':'Get method not allowed'}, 405)


class MotionAdDelete(ViewSet):
    authentication_classes = [SessionAuthentication, BasicAuthentication]
    permission_classes = [IsAuthenticated]
    def post(self, request):
        c_id = request.POST.get('c_id')
#        try:
        data = VerticalBannerAd.objects.get(id=c_id)
        data.delete()
        message="Delete Successfully"
        status = 204
#        except:
#            status=404
#            message="Delete Failed"
        return Response({'message':message}, status)
    
    def list(self, request):
        return Response({'message':'Get method not allowed'}, 405)


class BannerAdDelete(ViewSet):
    authentication_classes = [SessionAuthentication, BasicAuthentication]
    permission_classes = [IsAuthenticated]
    def post(self, request):
        c_id = request.POST.get('c_id')
#        try:
        data = HorizontalBannerAd.objects.get(id=c_id)
        data.delete()
        message="Delete Successfully"
        status = 204
#        except:
#            status=404
#            message="Delete Failed"
        return Response({'message':message}, status)
    
    def list(self, request):
        return Response({'message':'Get method not allowed'}, 405)


#class YoutubeSearch(ViewSet):
#    authentication_classes = [SessionAuthentication, BasicAuthentication]
#    permission_classes = [IsAuthenticated]
#    def post(self, request):
#        search_key = request.POST.get('search')
##        try:
#        data = YoutubeContent.objects.get(content_name)
#        data.delete()
#        message="Delete Successfully"
#        status = 204
##        except:
##            status=404
##            message="Delete Failed"
#        return Response({'message':message}, status)
#    
#    def list(self, request):
#        return Response({'message':'Get method not allowed'}, 405)
    
    
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
    message=''
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            print(username, password)
            user = authenticate(username=username, password=password)
            if user is not None:
                if user.is_admin:
                    login(request, user)
                    return redirect('boneadmin:dashboard')
                else:
                    return render(request, 'login.html', context={'form': AuthenticationForm(), 'message': 'This user is not an Admin!!'})
            else:
                message="Invalid username or password"
        else:
            message="Invalid username or password"
    return render(request, 'login.html', context={'form': AuthenticationForm(), 'message':message})

@login_required
@admin_required
@active_required
def admin_dashboard(request):
    youtube_video = YoutubeContent.objects.filter().count()
    total_user = User.objects.filter().count()
    context = {'dashboard':'active', 'total_user':total_user,
               'total_video': youtube_video}
    return render(request, 'dashboard.html', context)

@login_required
@admin_required
@active_required
def admin_bannerad(request):
    data=[]
    message=''
    if request.method == 'POST':
        req_type = request.POST.get('type')
        if req_type=='add_horizontalad':
            banner_name = request.POST.get('name')
            target_link = request.POST.get('link')
            file = request.FILES['banner']
            try:
                try:
                    data = HorizontalBannerAd.objects.create(banner_name=banner_name, 
                                     target_link=target_link, banner=file)
                    data.save()
                    message = "Conent Uploaded Successfully."
                except:
                    message = "File Uploaded Failed"
            except:
                message = "Please Select Valid Category"
        elif req_type=='search':
            key = request.POST.get('key')
            category = request.POST.get('category')
            try:
                video_data = HorizontalBannerAd.objects.get_queryset().order_by('created_at').reverse()
                if key:
                    search_data = video_data.filter(
                        Q(banner_name__icontains=key)
                        
                    ).distinct()
                     
                    video_data=search_data
                video_data =  page_data(request, video_data, 25)
                data = []
                for i in video_data:
                    data.append({
                                'id': i.id,
                                'content_name': i.content_name,
                                'content_link': i.content_link,
                                'category': i.category.category_name,
                                'content_poster': settings.MEDIA_URL+str(i.content_poster)
                            })
                page_value = {}
                page_value['has_previous'] = video_data.has_previous()
                page_value['has_next'] = video_data.has_next()
                page_value['num_pages'] = video_data.paginator.num_pages
                page_value['number'] = video_data.number
                if page_value['has_previous']:
                    page_value['previous_page_number'] = video_data.previous_page_number()
                if page_value['has_next']:
                    page_value['next_page_number'] = video_data.next_page_number()
    
                context = {
                    'object_list':page_value,
                    'video_data': video_data,
                    'status': 200,
                    'video_search': key,
                    'category': category
                }
                return HttpResponse(
                        json.dumps(context),
                        content_type="application/json"
                    )
            except:
                context = {
                    'object_list':'',
                    'video_data': '',
                    'status': 404,
                    'video_search': key,
                    'category': category
                }
                return HttpResponse(
                        json.dumps(context),
                        content_type="application/json"
                    )
# Load all other elements
    Hbanner = HorizontalBannerAd.objects.all()
    hbanner_data =  page_data(request, Hbanner, 25)
                
    page_value = {}
    page_value['has_previous'] = hbanner_data.has_previous()
    page_value['has_next'] = hbanner_data.has_next()
    page_value['num_pages'] = hbanner_data.paginator.num_pages
    page_value['number'] = hbanner_data.number
    if page_value['has_previous']:
        page_value['previous_page_number'] = hbanner_data.previous_page_number()
    if page_value['has_next']:
        page_value['next_page_number'] = hbanner_data.next_page_number()
            
    hbanner_list = []
    for i in hbanner_data:
        hbanner_list.append({
                    'id': i.id,
                    'banner_name': i.banner_name,
                    'banner': settings.MEDIA_URL+str(i.banner),
                    'postion': i.position,
                    'status': i.status
                })
    data = hbanner_list
    context = {'bannerad':'active', 
               'data':data, 
               'message':message,
               'object_list':page_value}
    return render(request, 'banner_ad.html', context)

@login_required
@admin_required
@active_required
def admin_motionad(request):
    data=[]
    message=''
    if request.method == 'POST':
        req_type = request.POST.get('type')
        if req_type=='add_verticalad':
            banner_name = request.POST.get('name')
            target_link = request.POST.get('link')
            file = request.FILES['banner']
            try:
                try:
                    data = VerticalBannerAd.objects.create(banner_name=banner_name, 
                                     target_link=target_link, banner=file)
                    data.save()
                    message = "Conent Uploaded Successfully."
                except:
                    message = "File Uploaded Failed"
            except:
                message = "Please Select Valid Category"
        elif req_type=='search':
            key = request.POST.get('key')
            category = request.POST.get('category')
            try:
                video_data = VerticalBannerAd.objects.get_queryset().filter().reverse()
                if key:
                    search_data = video_data.filter(
                        Q(banner_name__icontains=key)
                        
                    ).distinct()
                    video_data=search_data
                video_data =  page_data(request, video_data, 25)
                data = []
                for i in video_data:
                    data.append({
                                'id': i.id,
                                'content_name': i.content_name,
                                'content_link': i.content_link,
                                'category': i.category.category_name,
                                'content_poster': settings.MEDIA_URL+str(i.content_poster)
                            })
                page_value = {}
                page_value['has_previous'] = video_data.has_previous()
                page_value['has_next'] = video_data.has_next()
                page_value['num_pages'] = video_data.paginator.num_pages
                page_value['number'] = video_data.number
                if page_value['has_previous']:
                    page_value['previous_page_number'] = video_data.previous_page_number()
                if page_value['has_next']:
                    page_value['next_page_number'] = video_data.next_page_number()
    
                context = {
                    'object_list':page_value,
                    'video_data': data,
                    'status': 200,
                    'video_search': key,
                    'category': category
                }
                return HttpResponse(
                        json.dumps(context),
                        content_type="application/json"
                    )
            except:
                context = {
                    'object_list':'',
                    'video_data': '',
                    'status': 404,
                    'video_search': key,
                    'category': category
                }
                return HttpResponse(
                        json.dumps(context),
                        content_type="application/json"
                    )
# Load all other elements
    Vbanner = VerticalBannerAd.objects.all()
    vbanner_data =  page_data(request, Vbanner, 25)
                
    page_value = {}
    page_value['has_previous'] = vbanner_data.has_previous()
    page_value['has_next'] = vbanner_data.has_next()
    page_value['num_pages'] = vbanner_data.paginator.num_pages
    page_value['number'] = vbanner_data.number
    if page_value['has_previous']:
        page_value['previous_page_number'] = vbanner_data.previous_page_number()
    if page_value['has_next']:
        page_value['next_page_number'] = vbanner_data.next_page_number()
            
    hbanner_list = []
    for i in vbanner_data:
        hbanner_list.append({
                    'id': i.id,
                    'banner_name': i.banner_name,
                    'banner': settings.MEDIA_URL+str(i.banner),
                    'postion': i.position,
                    'status': i.status
                })
    data = hbanner_list
    context = {'bannerad':'active', 
               'data':data, 
               'message':message,
               'object_list':page_value}
    return render(request, 'motion_ad.html', context)


@login_required
@admin_required
@active_required
def admin_videoad(request):
    data=[]
    message=''
    if request.method == 'POST':
        req_type = request.POST.get('type')
        if req_type=='add_videoad':
            video_name = request.POST.get('name')
            file = request.FILES['video']
            try:
                try:
                    data = VideoAd.objects.create(video_name=video_name, 
                                     video=file)
                    data.save()
                    message = "Conent Uploaded Successfully."
                except:
                    message = "File Uploaded Failed"
            except:
                message = "Please Select Valid Category"
        elif req_type=='search':
            key = request.POST.get('key')
            category = request.POST.get('category')
            try:
                video_data = VideoAd.objects.get_queryset().order_by('created_at').reverse()
                if key:
                    search_data = video_data.filter(
                        Q(video_name__icontains=key)
                        
                    ).distinct()
                    video_data=search_data
                video_data =  page_data(request, video_data, 25)
                data = []
                for i in video_data:
                    data.append({
                                'id': i.id,
                                'content_name': i.content_name,
                                'content_link': i.content_link,
                                'category': i.category.category_name,
                                'content_poster': settings.MEDIA_URL+str(i.content_poster)
                            })
                page_value = {}
                page_value['has_previous'] = video_data.has_previous()
                page_value['has_next'] = video_data.has_next()
                page_value['num_pages'] = video_data.paginator.num_pages
                page_value['number'] = video_data.number
                if page_value['has_previous']:
                    page_value['previous_page_number'] = video_data.previous_page_number()
                if page_value['has_next']:
                    page_value['next_page_number'] = video_data.next_page_number()
    
                context = {
                    'object_list':page_value,
                    'video_data': data,
                    'status': 200,
                    'video_search': key,
                    'category': category
                }
                return HttpResponse(
                        json.dumps(context),
                        content_type="application/json"
                    )
            except:
                context = {
                    'object_list':'',
                    'video_data': '',
                    'status': 404,
                    'video_search': key,
                    'category': category
                }
                return HttpResponse(
                        json.dumps(context),
                        content_type="application/json"
                    )

# Load all other elements
    videos = VideoAd.objects.all()
    video_data =  page_data(request, videos, 25)
                
    page_value = {}
    page_value['has_previous'] = video_data.has_previous()
    page_value['has_next'] = video_data.has_next()
    page_value['num_pages'] = video_data.paginator.num_pages
    page_value['number'] = video_data.number
    if page_value['has_previous']:
        page_value['previous_page_number'] = video_data.previous_page_number()
    if page_value['has_next']:
        page_value['next_page_number'] = video_data.next_page_number()
            
    hbanner_list = []
    
    for i in video_data:
        hbanner_list.append({
                    'id': i.id,
                    'video_name': i.video_name,
                    'video': settings.MEDIA_URL+str(i.video),
                    'status': i.status
                })
    data = hbanner_list
    context = {'bannerad':'active', 
               'data':data, 
               'message':message,
               'object_list':page_value}
    return render(request, 'video_ad.html', context)

@login_required
@admin_required
@active_required
def admin_video_category(request):
    data=[]
    message=""
    if request.method == 'POST':
        video_category = request.POST.get('video_category')
        try:
            category = ContentCategory.objects.create(category_name=video_category)
            category.save()
            message="Video Category Create Successfully"
        except:
            message="Video Category Create Failed."
        
    videos = ContentCategory.objects.all()
#        videos = YoutubeContentSerializer(videos, many=True)
    Videoad_list = []
    for i in videos:
        Videoad_list.append({
                    'id': i.id,
                    'category_name': i.category_name,
                    'total_click': i.total_click,
                    'total_video': i.total_video
                })
    data = Videoad_list
    context = {'video_category':'active', 'data':data, 'message':message}
    return render(request, 'video_category.html', context)

@login_required
@admin_required
@active_required
def dashboard_base(request):
    
    return render(request, 'dashboard_base.html')

@login_required
@admin_required
@active_required
def admin_youtube(request):
    data=[]
    message=''
    if request.method == 'POST':
        req_type = request.POST.get('type')
        if req_type=='add_video':
            content_name = request.POST.get('name')
            content_link = request.POST.get('link')
            category = request.POST.get('video_category')
            desc = request.POST.get('desc')
            
            try:
                file = request.FILES['poster']
                category = ContentCategory.objects.get(id=category)
                try:
                    data = YoutubeContent.objects.create(content_name=content_name, 
                                     content_link=content_link, category=category,
                                     content_description=desc, content_poster=file)
                    data.save()
                    category.total_video+=1
                    category.save()
                    message = "Conent Uploaded Successfully."
                except:
                    message = "File Uploaded Failed"
            except:
                message = "Please Select Valid Category"
        elif req_type=='search':
            key = request.POST.get('key')
            category = request.POST.get('category')
            try:
                if category:
                    video_data = YoutubeContent.objects.get_queryset().filter(
                            category=category).reverse()
                else:
                    video_data = YoutubeContent.objects.get_queryset().order_by('created_at').reverse()
                if key:
                    search_data = video_data.filter(
                        Q(content_name__icontains=key)
                        
                    ).distinct()
                    if len(search_data)==0:
                        search_data = video_data.filter(
                            Q(content_description__icontains=key)
                            
                        ).distinct() 
                    video_data=search_data
                video_data =  page_data(request, video_data, 25)
                data = []
                for i in video_data:
                    data.append({
                                'id': i.id,
                                'content_name': i.content_name,
                                'content_link': i.content_link,
                                'category': i.category.category_name,
                                'content_poster': settings.MEDIA_URL+str(i.content_poster)
                            })
                page_value = {}
                page_value['has_previous'] = video_data.has_previous()
                page_value['has_next'] = video_data.has_next()
                page_value['num_pages'] = video_data.paginator.num_pages
                page_value['number'] = video_data.number
                if page_value['has_previous']:
                    page_value['previous_page_number'] = video_data.previous_page_number()
                if page_value['has_next']:
                    page_value['next_page_number'] = video_data.next_page_number()
    
                context = {
                    'object_list':page_value,
                    'video_data': data,
                    'status': 200,
                    'video_search': key,
                    'category': category
                }
                return HttpResponse(
                        json.dumps(context),
                        content_type="application/json"
                    )
            except:
                context = {
                    'object_list':'',
                    'video_data': '',
                    'status': 404,
                    'video_search': key,
                    'category': category
                }
                return HttpResponse(
                        json.dumps(context),
                        content_type="application/json"
                    )


# Load all other elements
            
    videos = YoutubeContent.objects.all().order_by('created_at').reverse()
    category = ContentCategory.objects.all().order_by('created_at').reverse()
#        videos = YoutubeContentSerializer(videos, many=True)
    
    video_data =  page_data(request, videos, 25)
                
    page_value = {}
    page_value['has_previous'] = video_data.has_previous()
    page_value['has_next'] = video_data.has_next()
    page_value['num_pages'] = video_data.paginator.num_pages
    page_value['number'] = video_data.number
    if page_value['has_previous']:
        page_value['previous_page_number'] = video_data.previous_page_number()
    if page_value['has_next']:
        page_value['next_page_number'] = video_data.next_page_number()
            
    video_list = []
    category_list = []
    for i in video_data:
        video_list.append({
                    'id': i.id,
                    'content_name': i.content_name,
                    'content_link': i.content_link,
                    'category': i.category.category_name,
                    'content_poster': settings.MEDIA_URL+str(i.content_poster)
                })
    for i in category:
        category_list.append({
                    'id': i.id,
                    'category_name': i.category_name,
                })
    data = video_list
    
    context = {'youtube':'active', 'data':data, 
               'message': message, 'category':category_list,
               'object_list':page_value}
    return render(request, 'youtube.html', context)

@login_required
@admin_required
@active_required
def logout_view(request):
    logout(request)
    return redirect('boneadmin:login')