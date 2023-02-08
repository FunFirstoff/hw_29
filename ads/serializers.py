from rest_framework import serializers

from ads.models import Ad


class AdListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ad
        fields = '__all__'
