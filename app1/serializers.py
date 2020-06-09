from rest_framework import serializers

from app1.models import User, Activity

# Making Activity Serializer
class ActivitySerializer(serializers.ModelSerializer):
    class Meta:
        model = Activity
        fields = ['log_in', 'log_out']


class UserSerializer(serializers.ModelSerializer):
    # Passing login Logout to User
    activity_periods = ActivitySerializer(many=True, read_only=True)

    class Meta:
        model = User
        fields = ['name', 'username','timezone', 'activity_periods']
