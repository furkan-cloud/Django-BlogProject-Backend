from rest_framework import serializers
from .models import Post, Comment

class PostSerializer(serializers.ModelSerializer):
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
            # "comment_count",
            # "like_count",
            # "postview_count"
        )

class CommentSerializer(serializers.ModelSerializer):
    # content = serializers.CharField()
    class Meta:
        model = Comment
        fields = (
            "content",
            "user",
            "post",
            "time_stamp"
        )
    
    # def create(self, validated_data):
    #     content = serializers.CharField()
    #     # content = validated_data["content"]
    #     return content

# class CommentSerializer
    


class PostDetailSerializer(serializers.ModelSerializer):
    comments = CommentSerializer(many=True)
    owner = serializers.SerializerMethodField(read_only=True)
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
            "owner"
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
            # "created_date",
            # "updated_date",
            "image",
            "author",
            "category",
            "status",
        )

class PostUpdateDeleteSerializer(serializers.ModelSerializer):
    
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

