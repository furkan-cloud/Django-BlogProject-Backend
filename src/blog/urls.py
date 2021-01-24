from django.urls import path
from .views import BlogList, PostDetail, PostCreate, PostUpdate, CommentCreate

urlpatterns = [
    path('', BlogList.as_view(), name="bloglist"),
    path('post/<str:slug>/', PostDetail.as_view(), name="postdetail"),
    path('create', PostCreate.as_view(), name="postcreate"),
    path('update/<int:pk>/', PostUpdate.as_view(), name="postupdate"),
    path('comment/<str:slug>/', CommentCreate, name="commentcreate"),
]
