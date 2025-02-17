from rest_framework import generics, permissions
from .models import Post, Comment, Category, Vote, User
from .serializers import PostSerializer, CommentSerializer, CategorySerializer, VoteSerializer, UserSerializer
from .permissions import IsAdminOrUser, IsAdminOrModeratorOrOwner

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
    serializer_class = PostSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

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