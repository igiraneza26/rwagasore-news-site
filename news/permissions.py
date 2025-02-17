from rest_framework import permissions

class IsAdminOrUser(permissions.BasePermission):
    """
    Allows only Admins and Regular Users to create posts.
    Moderators cannot create posts.
    """

    def has_permission(self, request, view):
        # Allow GET requests for everyone (public)
        if request.method in permissions.SAFE_METHODS:
            return True
        
        # Allow POST (create) only for Admins & Regular Users
        if request.user.is_authenticated:
            if request.user.groups.filter(name="Admin").exists():  # Admins can create posts
                return True
            if request.user.groups.filter(name="RegularUser").exists():  # Regular Users can create posts
                return True

        return False  # Deny if user is a Moderator or not logged in

class IsAdminOrModeratorOrOwner(permissions.BasePermission):
    """
    Allows only Admins, Moderators, or the Post Owner to delete a post.
    """

    def has_object_permission(self, request, view, obj):
        # Allow GET (read) requests for everyone
        if request.method in permissions.SAFE_METHODS:
            return True
        
        # Allow DELETE only for Admins, Moderators, or the Post Owner
        if request.user.is_authenticated:
            if request.user.groups.filter(name="Admin").exists():  # Admins can delete
                return True
            if request.user.groups.filter(name="Moderator").exists():  # Moderators can delete
                return True
            if obj.author == request.user:  # Post Owners can delete their own posts
                return True
        
        return False  # Deny for all others
    
class IsAdminUser(permissions.BasePermission):
    """Allows only Admins full access"""
    def has_permission(self, request, view):
        return request.user.is_authenticated and request.user.groups.filter(name="Admin").exists()

class IsModerator(permissions.BasePermission):
    """Allows Moderators to edit/delete posts"""
    def has_permission(self, request, view):
        return request.user.is_authenticated and request.user.groups.filter(name="Moderator").exists()