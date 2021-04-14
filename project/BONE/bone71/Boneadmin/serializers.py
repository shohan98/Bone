from rest_framework import serializers
from .models import (ContentCategory, ContentClickMonthlyReport, YoutubeContent,
                     VerticalAdWatchMonthlyReport, VerticalBannerAd,
                     HorizontalAdWatchMonthlyReport, HorizontalBannerAd,
                     VideoAdWatchMonthlyReport, VideoAd)


class ContentCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = ContentCategory
        fields = '__all__'


class ContentClickMonthlyReportSerializer(serializers.ModelSerializer):
    class Meta:
        model = ContentClickMonthlyReport
        fields = '__all__'


class YoutubeContentSerializer(serializers.ModelSerializer):
    class Meta:
        model = YoutubeContent
        fields = '__all__'


class VerticalAdWatchMonthlyReportSerializer(serializers.ModelSerializer):
    class Meta:
        model = VerticalAdWatchMonthlyReport
        fields = '__all__'


class VerticalBannerAdSerializer(serializers.ModelSerializer):
    class Meta:
        model = VerticalBannerAd
        fields = '__all__'


class HorizontalAdWatchMonthlyReportSerializer(serializers.ModelSerializer):
    class Meta:
        model = HorizontalAdWatchMonthlyReport
        fields = '__all__'


class HorizontalBannerAdSerializer(serializers.ModelSerializer):
    class Meta:
        model = HorizontalBannerAd
        fields = '__all__'


class VideoAdWatchMonthlyReportSerializer(serializers.ModelSerializer):
    class Meta:
        model = VideoAdWatchMonthlyReport
        fields = '__all__'


class VideoAdSerializer(serializers.ModelSerializer):
    class Meta:
        model = VideoAd
        fields = '__all__'
