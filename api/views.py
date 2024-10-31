from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import User, Blogpost
from .serializer import UserSerializer, BlogPostSerializer  # Changed from 'serializer' to 'serializers'
from rest_framework import generics
 

@api_view(['GET'])
def get_users(request):
    # user_data = {"name": "Tukur", "age": 15}
    # serializer = UserSerializer(data=user_data)
       # if serializer.is_valid():
    #    return Response(serializer.data)
    # return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    users = User.objects.all()
    serializer = UserSerializer(users, many = True)
    return Response(serializer.data)
    
        
@api_view(['POST'])
def create_user(request):
    serializer = UserSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED )
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'DELETE'])
def user_detail(request, pk):
    try:
        user = User.objects.get(pk=pk)
    except User.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    if request.method == 'GET':
        serializer = UserSerializer(user)
        return Response(serializer.data)
    
    elif request.method == 'PUT':
        serializer = UserSerializer(user, data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    elif request.method == 'DELETE':
        user.delete()
        return Response(status = status.HTTP_204_NO_CONTENT)
    


class BlogPostListCreate(generics.ListCreateAPIView):
    queryset = Blogpost.objects.all()
    serializer_class = BlogPostSerializer

    def delete(self, request, *args, **kwargs):
        Blogpost.objects.all().delete()
        return Response(status= status.HTTP_204_NO_CONTENT)
    
class BlogPostListViews(generics.ListAPIView):
    queryset = Blogpost.objects.all()
    serializer_class = BlogPostSerializer


class BlogPostRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = Blogpost.objects.all()
    serializer_class = BlogPostSerializer
    lookup_field = "pk"



class BlogPostList(APIView):

    def get(self, request, format = None):
        title =  request.query_params.get("title", "")
        if title:
            blog_posts = Blogpost.objects.filter(title__icontains = title)
        else:
            blog_posts = Blogpost.objects.all()

        serializer = BlogPostSerializer(blog_posts, many = True)
        return Response(serializer.data, status=status.HTTP_200_OK)
   
