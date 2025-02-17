from rest_framework import serializers
from .models import Post, Comment, Category, Vote, User

# Category Serializer
class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'  # Includes all fields

# Post Serializer
class PostSerializer(serializers.ModelSerializer):
    category = CategorySerializer(read_only=True)  # Include category details
    author = serializers.StringRelatedField()  # Show author's username

    class Meta:
        model = Post
        fields = '__all__'  # Includes all fields

# Comment Serializer
class CommentSerializer(serializers.ModelSerializer):
    author = serializers.StringRelatedField()

    class Meta:
        model = Comment
        fields = '__all__'

# Vote Serializer
class VoteSerializer(serializers.ModelSerializer):
    user = serializers.StringRelatedField()

    class Meta:
        model = Vote
        fields = '__all__'
        
# User Serializer
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'is_staff', 'date_joined']