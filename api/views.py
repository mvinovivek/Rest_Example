from rest_framework import viewsets, filters
from .serializers import NoteSerializer,UserSerializer
from django.contrib.auth.models import User
from .models import Note
from rest_framework import permissions
from django_filters.rest_framework import DjangoFilterBackend

class IsOwnerOrReadOnly(permissions.BasePermission):
    """
    Custom permission to only allow owners of an object to edit it.
    """

    def has_object_permission(self, request, view, obj):
        # Read permissions are allowed to any request,
        # so we'll always allow GET, HEAD or OPTIONS requests.
        # if request.method in permissions.SAFE_METHODS:
        #     return True

        # Write permissions are only allowed to the owner of the snippet.
        return obj.owner == request.user

class IsOwnerFilterBackend(filters.BaseFilterBackend):
    """
    Filter that only allows users to see their own objects.
    """
    def filter_queryset(self, request, queryset, view):
        return queryset.filter(owner=request.user)



class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class NoteViewSet(viewsets.ModelViewSet):
    queryset = Note.objects.all()
    serializer_class = NoteSerializer
    permission_classes=[IsOwnerOrReadOnly]
    filter_backends=[DjangoFilterBackend,IsOwnerFilterBackend]
