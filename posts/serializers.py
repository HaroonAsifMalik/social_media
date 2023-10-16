from rest_framework import serializers
from .models import Post, Comment, Like, Share  # Import your models
from django.contrib.auth.models import User  # Import User model

class LikeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Like
        fields = '__all__'

class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = '__all__'

class ShareSerializer(serializers.ModelSerializer):
    class Meta:
        model = Share
        fields = '__all__'

class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = '__all__'

    author = serializers.PrimaryKeyRelatedField(queryset=User.objects.all())
    likes = LikeSerializer(many=True, read_only=True)
    comments = CommentSerializer(many=True, read_only=True)
    shares = ShareSerializer(many=True, read_only=True)
