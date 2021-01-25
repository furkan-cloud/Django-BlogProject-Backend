from django.shortcuts import get_object_or_404, render
from rest_framework import generics
from .models import Post, Comment, Like, PostView
from .serializers import PostSerializer, PostDetailSerializer, PostCreateSerializer, PostUpdateDeleteSerializer, CommentSerializer
from .pagination import MyPagination
from rest_framework.permissions import IsAuthenticated
from .permissions import UpdateDeletePermission

from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
# Create your views here.

class BlogList(generics.ListAPIView):
    serializer_class = PostSerializer
    queryset = Post.objects.all()
    pagination_class = MyPagination

class PostDetail(generics.RetrieveAPIView):
    serializer_class = PostDetailSerializer
    lookup_field = "slug"
    permission_classes = [IsAuthenticated]


    def get_queryset(self):
        queryset = Post.objects.all()
        slug = self.kwargs["slug"]
        queryset = queryset.filter(slug = slug)
        return queryset

# class PostDetail(generics.RetrieveAPIView):
    
#     serializer_class = PostSerializer

#     def get_object(self, queryset=None, **kwargs):
#         item = self.kwargs.get('pk')
#         return get_object_or_404(Post, slug=item)

class PostCreate(generics.CreateAPIView):
    serializer_class = PostCreateSerializer
    queryset = Post.objects.all()
    permission_classes = [IsAuthenticated]

class PostUpdate(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = PostUpdateDeleteSerializer
    queryset = Post.objects.all()
    # lookup_field = "slug"
    permission_classes = [IsAuthenticated, UpdateDeletePermission]

# class CommentCreate(generics.CreateAPIView):
#     serializer_class = CommentSerializer
#     queryset = Comment.objects.all()
#     permission_classes = [IsAuthenticated]
#     lookup_field = "id"

    # def get_queryset(self):
    #     queryset = Post.objects.all()
    #     title = self.kwargs["title"]
    #     queryset = queryset.filter(title = title)
    #     return queryset

@api_view(["GET", "POST"])
def CommentCreate(request, slug):
    
    if request.method == "GET":
        post = get_object_or_404(Post, slug=slug)
        comments = Comment.objects.filter(post=post)
        serializer = CommentSerializer(comments, many=True)
        return Response(serializer.data)

    elif request.method == "POST":
        post = get_object_or_404(Post, slug=slug)
        if request.user == post.author:
            return Response(
                {'message': 'You are the owner of this post!'},  status=status.HTTP_403_FORBIDDEN
            )

        serializer = CommentSerializer(data=request.data)
        if serializer.is_valid():
            # student = form.save(commit=False)
            # student.teacher = request.user
            # student.save()
            serializer.save(post=post, user=request.user)
            data = {
                "message": "Comment created succesfully"
            }
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)





# class LikeView(generics.RetrieveAPIView):
#     serializer_class = PostSerializer
#     queryset = Like.objects.all()

class PostViewSeen(generics.RetrieveAPIView):
    serializer_class = PostSerializer
    queryset = PostView.objects.all()

# def PostViewSeen(request, slug):
#     post = get_object_or_404(Post, slug=slug)
#     postview = Post.objects.filter(post=post)





# @login_required()
@api_view(["POST"])
def LikeView(request, slug):
    if request.method == 'POST':
        post = get_object_or_404(Post, slug=slug)
        like_qs = Like.objects.filter(user=request.user, post=post)
        if like_qs.exists():
            like_qs[0].delete()
            data = {
                "message": "Like deleted!"
            }
            return Response(data, status=status.HTTP_204_NO_CONTENT)
        else:
            Like.objects.create(user=request.user, post=post)
            data = {
                "message": "Liked!"
            }
            return Response(data, status=status.HTTP_201_CREATED)

