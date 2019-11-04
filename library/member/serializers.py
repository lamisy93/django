from rest_framework import serializers, fields
from . import models

class AvatarSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Avatar
        fields = ('member', 'photo')

class MemberSerializer(serializers.ModelSerializer):

    avatars = AvatarSerializer(source='avatar_set', many=True)

    class Meta:
        model = models.Member
        fields = ('firstname', 'lastname','email','avatars')