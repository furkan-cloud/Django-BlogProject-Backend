from rest_framework import serializers
from .models import Post, Comment

class PostSerializer(serializers.ModelSerializer):
    # author = serializers.CharField()
    author = serializers.StringRelatedField()
    category = serializers.SerializerMethodField()
    class Meta:
        model = Post
        fields = (
            "title",
            "description",
            "created_date",
            "updated_date",
            "image",
            "author",
            "category",
            "comment_count",
            "like_count",
            "postview_count",
            "slug"
        )

    def get_category(self, obj):
        return obj.category.name

# class CommentSerializer(serializers.ModelSerializer):
#     user = serializers.CharField( source="user.username", read_only=True)
#     post = serializers.SerializerMethodField()
#     # user = serializers.CharField()
#     # content = serializers.CharField()
#     class Meta:
#         model = Comment
#         fields = (
#             "content",
#             "user",
#             "post_id",
#             "time_stamp"
#         )
class CommentSerializer(serializers.ModelSerializer):
    # url = serializers.HyperlinkedIdentityField(
    #     view_name='commentcreate',
    #     # lookup_field='slug'
    # )
    user = serializers.CharField( source="user.username", read_only=True)
    post = serializers.SerializerMethodField()

    class Meta:
        model = Comment
        fields = [            "content",
            "user",
            "post",
            "time_stamp"]

    def get_post(self, obj):
        return obj.post.id

    # def getPost(self,obj, request):
    #     return obj.post.objects.all()

    # def create(self, validated_data):
    #     content = serializers.CharField()
    #     # content = validated_data["content"]
    #     return content

# class CommentSerializer
    


class PostDetailSerializer(serializers.ModelSerializer):
    comments = CommentSerializer(many=True)
    owner = serializers.SerializerMethodField(read_only=True)
    author = serializers.StringRelatedField()
    category = serializers.StringRelatedField()
    class Meta:
        model = Post
        fields = (
            "title",
            "description",
            "created_date",
            "updated_date",
            "image",
            "author",
            "category",
            "comments",
            "comment_count",
            "like_count",
            "postview_count",
            "owner",
            "slug"
        )
        # depth = 1

    def get_owner(self, obj):
        request = self.context["request"]
        if request.user.is_authenticated:
            if obj.author == request.user:
                return True
            return False

class PostCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = (
            "title",
            "description",
            "image",
            "author",
            "category",
            "status",
        )

class PostUpdateDeleteSerializer(serializers.ModelSerializer):
    author = serializers.StringRelatedField()
    category = serializers.StringRelatedField()
    
    class Meta:
        model = Post
        fields = (
            "title",
            "description",
            "created_date",
            "updated_date",
            "image",
            "author",
            "category",
        )
        # lookup_fields = ['title']

