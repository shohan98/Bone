from rest_framework import serializers
from .models import (ContentCategory, ContentClickMonthlyReport, YoutubeContent,
                     VerticalAdWatchMonthlyReport, VerticalBannerAd,
                     HorizontalAdWatchMonthlyReport, HorizontalBannerAd,
                     VideoAdWatchMonthlyReport, VideoAd)


class ContentCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model=ContentCategory
        field='__all__'
        
class ContentClickMonthlyReportSerializer(serializers.ModelSerializer):
    class Meta:
        model=ContentClickMonthlyReport
        field='__all__'
        
class YoutubeContentSerializer(serializers.ModelSerializer):
    class Meta:
        model=YoutubeContent
        field='__all__'
        
class VerticalAdWatchMonthlyReportSerializer(serializers.ModelSerializer):
    class Meta:
        model=VerticalAdWatchMonthlyReport
        field='__all__'
        
class VerticalBannerAdSerializer(serializers.ModelSerializer):
    class Meta:
        model=VerticalBannerAd
        field='__all__'
        
class HorizontalAdWatchMonthlyReportSerializer(serializers.ModelSerializer):
    class Meta:
        model=HorizontalAdWatchMonthlyReport
        field='__all__'
        
class HorizontalBannerAdSerializer(serializers.ModelSerializer):
    class Meta:
        model=HorizontalBannerAd
        field='__all__'
        
class VideoAdWatchMonthlyReportSerializer(serializers.ModelSerializer):
    class Meta:
        model=VideoAdWatchMonthlyReport
        field='__all__'
        
class VideoAdSerializer(serializers.ModelSerializer):
    class Meta:
        model=VideoAd
        field='__all__'
                