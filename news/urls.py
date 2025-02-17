from django.urls import path, include
from .views import CategoryListView, PostListCreateView, PostDetailView, CommentListCreateView, VoteListCreateView, UserListView
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

urlpatterns = [
    path('categories/', CategoryListView.as_view(), name='category-list'),
    path('posts/', PostListCreateView.as_view(), name='post-list-create'),
    path('posts/<int:pk>/', PostDetailView.as_view(), name='post-detail'),
    path('comments/', CommentListCreateView.as_view(), name='comment-list-create'),
    path('votes/', VoteListCreateView.as_view(), name='vote-list-create'),
    path('users/', UserListView.as_view(), name='user-list'),  # Endpoint to list all users
    # Authentication Routes
    path('auth/login/', TokenObtainPairView.as_view(), name='token_obtain_pair'),  # Login (JWT Token)
    path('auth/refresh/', TokenRefreshView.as_view(), name='token_refresh'),  # Refresh token
    path('auth/register/', include('dj_rest_auth.registration.urls')),  # User Registration
]