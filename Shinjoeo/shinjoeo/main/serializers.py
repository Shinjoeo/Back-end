from dataclasses import field
from .models import NewWord, NewWord_user
from rest_framework import serializers

class LikeUserSerializer(serializers.ModelSerializer):
    class Meta:
        model=NewWord_user
        field='__all__'

class NewWordSerializer(serializers.ModelSerializer):
    like_ids=LikeUserSerializer(many=True)
    class Meta:
        model=NewWord
        fields= ['like_ids']
    