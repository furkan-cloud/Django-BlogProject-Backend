from django.shortcuts import render
from rest_framework import generics
from .models import Post
from .serializers import PostSerializer, PostDetailSerializer, PostCreateSerializer, PostUpdateDeleteSerializer

# Create your views here.

class BlogList(generics.ListAPIView):
    serializer_class = PostSerializer
    queryset = Post.objects.all()

class PostDetail(generics.RetrieveAPIView):
    serializer_class = PostDetailSerializer
    lookup_field = "title"

    def get_queryset(self):
        queryset = Post.objects.all()
        title = self.kwargs["title"]
        queryset = queryset.filter(title = title)
        return queryset

class PostCreate(generics.CreateAPIView):
    serializer_class = PostCreateSerializer
    queryset = Post.objects.all()

class PostUpdate(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = PostUpdateDeleteSerializer
    queryset = Post.objects.all()
    lookup_field = "id"
    
    # def get_queryset(self):
    #     queryset = Post.objects.all()
    #     title = self.kwargs["title"]
    #     queryset = queryset.filter(title = title)
    #     return queryset

