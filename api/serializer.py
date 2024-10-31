from rest_framework import serializers
from .models import User, Blogpost

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'

class BlogPostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Blogpost
        fields = '__all__'


      