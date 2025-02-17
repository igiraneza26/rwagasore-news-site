from django.shortcuts import render, get_object_or_404, redirect
from rest_framework import generics, permissions
from .models import Post, Comment, Category, Vote, User
from .serializers import PostSerializer, CommentSerializer, CategorySerializer, VoteSerializer, UserSerializer
from .permissions import IsAdminOrUser, IsAdminOrModeratorOrOwner, IsAdminUser, IsModerator
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.utils.decorators import method_decorator
from django.views import View
from django.middleware.csrf import get_token
from rest_framework.permissions import BasePermission, IsAuthenticated
from django.contrib.auth.models import Group

# Category API View
class CategoryListView(generics.ListCreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

# Post API View (List & Create)
class PostListCreateView(generics.ListCreateAPIView):
    queryset = Post.objects.all().order_by('-created_at')  # Latest posts first
    serializer_class = PostSerializer
    permission_classes = [IsAdminOrUser]  # Only Admins & Regular Users can create posts
    def perform_create(self, serializer):
        serializer.save(author=self.request.user)  # Automatically assigns logged-in user as author

# Post API View (Retrieve, Update, Delete)
class PostDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer #View fro all users to see posts
    
# View for Admins  and Moderators to edit/delete posts
class UpdatePostView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [IsAdminUser | IsModerator] #View fro all users to see posts

# Comment API View (List & Create)
class CommentListCreateView(generics.ListCreateAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = [IsAdminOrModeratorOrOwner]  # Restrict delete access

# Vote API View (Upvote/Downvote)
class VoteListCreateView(generics.ListCreateAPIView):
    queryset = Vote.objects.all()
    serializer_class = VoteSerializer
    permission_classes = [permissions.IsAuthenticated]

# User API View (View)
class UserListView(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAdminUser]  # Only Admins can view user list
    
def home(request):
    posts = Post.objects.all()
    return render(request, "news/home.html", {"posts": posts})

def post_detail(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    return render(request, "news/post_detail.html", {"post": post})

@login_required
def add_comment(request, post_id):
    if request.method == "POST":
        post = get_object_or_404(Post, id=post_id)
        Comment.objects.create(post=post, author=request.user, text=request.POST["text"])
    return redirect("post_detail", post_id=post.id)

# Get all posts
def get_posts(request):
    posts = Post.objects.all().values("id", "title", "content", "author__username", "created_at")
    return JsonResponse(list(posts), safe=False)

# Get a single post with comments
def get_post(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    comments = Comment.objects.filter(post=post).values("id", "text", "author__username", "created_at")
    return JsonResponse({"post": post.title, "content": post.content, "author": post.author.username, "comments": list(comments)})

# Upvote/Downvote Post
@csrf_exempt
def vote_post(request, post_id):
    if request.method == "POST":
        data = json.loads(request.body)
        post = get_object_or_404(Post, id=post_id)
        if data.get("vote") == "up":
            post.upvotes += 1
        elif data.get("vote") == "down":
            post.downvotes += 1
        post.save()
        return JsonResponse({"votes": post.upvotes - post.downvotes})

# Handle User Authentication (Login)
@csrf_exempt
def login_user(request):
    if request.method == "POST":
        data = json.loads(request.body)
        user = authenticate(username=data["username"], password=data["password"])
        if user:
            login(request, user)
            return JsonResponse({"message": "Login successful", "user": user.username})
        return JsonResponse({"error": "Invalid credentials"}, status=401)

# Handle Logout
def logout_user(request):
    logout(request)
    return JsonResponse({"message": "Logged out successfully"})

# Register New User
@csrf_exempt
def register_user(request):
    if request.method == "POST":
        data = json.loads(request.body)
        user = User.objects.create_user(username=data["username"], password=data["password"])
        return JsonResponse({"message": "User registered successfully", "user": user.username})
    
class IsAdminUser(BasePermission):
    """Allows only Admins full access"""
    def has_permission(self, request, view):
        return request.user.is_authenticated and request.user.groups.filter(name="Admin").exists()

class IsModerator(BasePermission):
    """Allows Moderators to edit/delete posts"""
    def has_permission(self, request, view):
        return request.user.is_authenticated and request.user.groups.filter(name="Moderator").exists()

class IsRegularUser(BasePermission):
    """Allows Regular Users to create/view posts but not edit/delete"""
    def has_permission(self, request, view):
        return request.user.is_authenticated and request.user.groups.filter(name="RegularUser").exists()