from rest_framework import generics, permissions
from instapaws_api.permissions import IsOwnerOrReadOnly
from .models import Like
from .serializers import LikeSerializer

# Create your views here.
