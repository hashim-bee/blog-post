from django.urls import path
from . views import *

urlpatterns = [
    path('',Home,name='home'),
    path('create/', createpost.as_view(),name='create-post'),
    path('posts/', listPosts.as_view(), name='post-posts')
]
