from rest_framework import serializers

from app1.models import User


class userSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'

