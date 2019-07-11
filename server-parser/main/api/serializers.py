from rest_framework import serializers
from django.contrib.auth import get_user_model
from .models import Profile


class UserCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = get_user_model()
        fields = ['username', 'password']
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        User = get_user_model()
        username = validated_data['username']
        password = validated_data['password']

        user_obj = User(username=username)
        user_obj.set_password(password)
        user_obj.save()

        profile = Profile(user=user_obj)
        profile.save()

        return validated_data