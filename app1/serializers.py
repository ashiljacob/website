from rest_framework import serializers

from app1.models import User, Activity

# Making Activity Serializer
class ActivitySerializer(serializers.ModelSerializer):
    class Meta:
        model = Activity
        fields = ['log_in', 'log_out']


class UserSerializer(serializers.ModelSerializer):
    # Passing Activities Of User
    activity_periods = ActivitySerializer(many=True,read_only=False)

    class Meta:
        model = User
        fields = ['name', 'username','timezone', 'activity_periods']

    # For Adding Post Data Of Activity in request , Overriding create method
    def create(self, validated_data):
        act = validated_data.pop('activity_periods')
        user = User.objects.create(**validated_data)
        # Looping through Activities
        for i in act:
            Activity.objects.create(user=user, **i)
        return user
