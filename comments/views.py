from rest_framework import generics, permissions
from django_filters.rest_framework import DjangoFilterBackend
from instapaws_api.permissions import IsOwnerOrReadOnly
from .models import Comment
from .serializers import CommentSerializer, CommentDetailSerializer

# Create your views here.
