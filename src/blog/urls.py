from django.urls import path
from .views import BlogList, PostDetail, PostCreate, PostUpdate

urlpatterns = [
    path('', BlogList.as_view(), name="bloglist"),
    path('post/<title>', PostDetail.as_view(), name="postdetail"),
    path('create', PostCreate.as_view(), name="postcreate"),
    path('update/<int:id>', PostUpdate.as_view(), name="postupdate"),
]
