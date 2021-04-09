from django.db import models
from django.utils import timezone as tz
from django.contrib.auth.models import AbstractUser


# Create your models here.
class ContentCategory(models.Model):
    category_name = models.CharField(max_length=60)
    total_video   = models.IntegerField(default=0)
    total_click   = models.IntegerField(default=0)
    added_by_ip   = models.CharField(max_length=25)
    created_at    = models.DateTimeField(default=tz.now)
    
    def __str__(self):
        return self.category_name
    

class YoutubeContent(models.Model):
    content_name    = models.CharField(max_length=600)
    category        = models.ForeignKey(ContentCategory, on_delete=models.CASCADE)
    content_link    = models.URLField()
    total_click     = models.IntegerField(default=0)
    status          = models.BooleanField(default=True)
    added_by_ip     = models.CharField(max_length=25)
    created_at      = models.DateTimeField(default=tz.now)
    
    def __str__(self):
        return self.content_name

class VideoAd(models.Model):
    video_name      = models.CharField(max_length=300)
    video           = models.FileField()
    total_watch     = models.IntegerField(default=0)
    status          = models.BooleanField(default=True)
    added_by_ip     = models.CharField(max_length=25)
    created_at      = models.DateTimeField(default=tz.now)
    
    def __str__(self):
        return self.video_name

class VerticalBannerAd(models.Model):
    banner_name     = models.CharField(max_length=300)
    banner          = models.FileField()
    target_link      = models.URLField(null=True)
    total_watch     = models.IntegerField(default=0)
    status          = models.BooleanField(default=True)
    position        = models.IntegerField(default=0)
    added_by_ip     = models.CharField(max_length=25)
    created_at      = models.DateTimeField(default=tz.now)
    
    def __str__(self):
        return self.banner_name

class HorizontalBannerAd(models.Model):
    banner_name      = models.CharField(max_length=300)
    banner           = models.FileField()
    target_link      = models.URLField(null=True)
    total_watch     = models.IntegerField(default=0)
    status          = models.BooleanField(default=True)
    position        = models.IntegerField(default=0)
    added_by_ip     = models.CharField(max_length=25)
    created_at      = models.DateTimeField(default=tz.now)
    
    def __str__(self):
        return self.banner_name

class ContentClickMonthlyReport(models.Model):
    content         = models.ForeignKey(YoutubeContent, on_delete=models.CASCADE)
    report_date     = models.CharField(max_length=30)
    total_click     = models.IntegerField(default=0)
    created_at      = models.DateTimeField(default=tz.now)
    
    def __str__(self):
        return self.report_date

class VideoAdWatchMonthlyReport(models.Model):
    content         = models.ForeignKey(VideoAd, on_delete=models.CASCADE)
    report_date     = models.CharField(max_length=30)
    total_watch     = models.IntegerField(default=0)
    created_at      = models.DateTimeField(default=tz.now)
    
    def __str__(self):
        return self.report_date

class VerticalAdWatchMonthlyReport(models.Model):
    content         = models.ForeignKey(VerticalBannerAd, on_delete=models.CASCADE)
    report_date     = models.CharField(max_length=30)
    total_watch     = models.IntegerField(default=0)
    total_click     = models.IntegerField(default=0)
    created_at      = models.DateTimeField(default=tz.now)
    
    def __str__(self):
        return self.report_date

class HorizontalAdWatchMonthlyReport(models.Model):
    content         = models.ForeignKey(HorizontalBannerAd, on_delete=models.CASCADE)
    report_date     = models.CharField(max_length=30)
    total_watch     = models.IntegerField(default=0)
    total_click     = models.IntegerField(default=0)
    created_at      = models.DateTimeField(default=tz.now)
    
    def __str__(self):
        return self.report_date

