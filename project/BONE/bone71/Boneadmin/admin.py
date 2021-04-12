from django.contrib import admin
from .models import (YoutubeContent, VideoAd, VideoAdWatchMonthlyReport,
                     HorizontalBannerAd, HorizontalAdWatchMonthlyReport,
                     VerticalBannerAd, VerticalAdWatchMonthlyReport,
                     ContentCategory, ContentClickMonthlyReport, User, Admin)

# Register your models here.

class UserAdmin(admin.ModelAdmin):
    list_display = ['username', 'email', 'is_admin', 'is_user']
    search_fields = ['email']


class YoutubeContentAdmin(admin.ModelAdmin):
    list_display = ['content_name', 'category', 'total_click', 'status',
                    'created_at']
    search_fields = ['content_name']
    list_filter = ('category',)

class VideoAdAdmin(admin.ModelAdmin):
    list_display = ['video_name', 'total_watch', 'status']
    search_fields = ['video_name',]

class VideoAdWatchMonthlyReportAdmin(admin.ModelAdmin):
    list_display = ['content', 'report_date', 'total_watch']
    search_fields = ['content', 'report_date']

class HorizontalBannerAdAdmin(admin.ModelAdmin):
    list_display = ['banner_name', 'target_link', 'total_watch', 'status', 
                    'position', 'created_at']
    search_fields = ['banner_name',]

class HorizontalAdWatchMonthlyReportAdmin(admin.ModelAdmin):
    list_display = ['content', 'report_date', 'total_watch', 'total_click']
    search_fields = ['content', 'report_date']

class VerticalBannerAdAdmin(admin.ModelAdmin):
    list_display = ['banner_name', 'target_link', 'total_watch', 'status', 
                    'position', 'created_at']
    search_fields = ['banner_name',]

class VerticalAdWatchMonthlyReportAdmin(admin.ModelAdmin):
    list_display = ['content', 'report_date', 'total_watch', 'total_click']
    search_fields = ['content', 'report_date']

class ContentCategoryAdmin(admin.ModelAdmin):
    list_display = ['category_name', 'total_video', 'total_click']
    search_fields = ['category_name',]

class ContentClickMonthlyReportAdmin(admin.ModelAdmin):
    list_display = ['content', 'report_date', 'total_click']
    search_fields = ['content', 'report_date']

admin.site.register(User, UserAdmin)
admin.site.register(Admin)
admin.site.register(YoutubeContent, YoutubeContentAdmin)
admin.site.register(VideoAd, VideoAdAdmin)
admin.site.register(VideoAdWatchMonthlyReport, VideoAdWatchMonthlyReportAdmin)
admin.site.register(HorizontalBannerAd, HorizontalBannerAdAdmin)
admin.site.register(HorizontalAdWatchMonthlyReport,HorizontalAdWatchMonthlyReportAdmin)
admin.site.register(VerticalBannerAd, VerticalBannerAdAdmin)
admin.site.register(VerticalAdWatchMonthlyReport, VerticalAdWatchMonthlyReportAdmin)
admin.site.register(ContentCategory, ContentCategoryAdmin)
admin.site.register(ContentClickMonthlyReport, ContentClickMonthlyReportAdmin)