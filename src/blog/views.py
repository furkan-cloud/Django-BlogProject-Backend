from django.shortcuts import render
from rest_framework import generics
from .models import Post, Comment, Like, PostView
from .serializers import PostSerializer, PostDetailSerializer, PostCreateSerializer, PostUpdateDeleteSerializer, CommentSerializer
from .pagination import MyPagination
from rest_framework.permissions import IsAuthenticated
from .permissions import UpdateDeletePermission
# Create your views here.

class BlogList(generics.ListAPIView):
    serializer_class = PostSerializer
    queryset = Post.objects.all()
    pagination_class = MyPagination

class PostDetail(generics.RetrieveAPIView):
    serializer_class = PostDetailSerializer
    lookup_field = "title"
    permission_classes = [IsAuthenticated]


    def get_queryset(self):
        queryset = Post.objects.all()
        title = self.kwargs["title"]
        queryset = queryset.filter(title = title)
        return queryset

class PostCreate(generics.CreateAPIView):
    serializer_class = PostCreateSerializer
    queryset = Post.objects.all()
    permission_classes = [IsAuthenticated]

class PostUpdate(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = PostUpdateDeleteSerializer
    queryset = Post.objects.all()
    lookup_field = "id"
    permission_classes = [IsAuthenticated, UpdateDeletePermission]

class CommentCreate(generics.CreateAPIView):
    serializer_class = CommentSerializer
    queryset = Comment.objects.all()
    permission_classes = [IsAuthenticated]

    # def get_queryset(self):
    #     queryset = Post.objects.all()
    #     title = self.kwargs["title"]
    #     queryset = queryset.filter(title = title)
    #     return queryset

class LikeView(generics.RetrieveAPIView):
    serializer_class = PostSerializer
    queryset = Like.objects.all()

class PostViewSeen(generics.RetrieveAPIView):
    serializer_class = PostSerializer
    queryset = PostView.objects.all()

