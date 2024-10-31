from django.urls import path
from .views import get_users, create_user, user_detail, BlogPostListCreate, BlogPostRetrieveUpdateDestroy, BlogPostListViews, BlogPostList

urlpatterns = [
    path('users/', get_users, name= 'get_users'),
    path('users/create', create_user, name= 'create_user'),
    path('users/<int:pk>', user_detail, name= 'user_detail'),
    path('users/blogposts/', BlogPostListCreate.as_view(), name= 'blogpost_view_create'),
    path('users/blogposts/get/', BlogPostList.as_view(), name= 'blogposts_custom_get'),
    path('users/blogposts/customget/', BlogPostListViews.as_view(), name= 'blogposts_view_get'),
    path('users/blogposts/<int:pk>', BlogPostRetrieveUpdateDestroy.as_view(), name= 'retrieve_update_delete')
    
]
