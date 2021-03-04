from rest_framework.serializers import ModelSerializer
from rest_framework import serializers
from .models import Profile


class ProfileSerializer(ModelSerializer):
    card_id = serializers.CharField(max_length=16, min_length=16)
    pin = serializers.CharField(max_length=4, min_length=4)

    class Meta:
        model = Profile
        fields = ['id', 'card_id', 'employee_id', 'name', 'email', 'mobile',
                  'pin', 'balance']
