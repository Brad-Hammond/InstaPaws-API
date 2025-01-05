from rest_framework import generics, permissions
from instapaws_api.permissions import IsOwnerOrReadOnly
from .models import Like
from .serializers import LikeSerializer

# Create your views here.
class LikeList(generics.ListCreateAPIView):

    serializer_class = LikeSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    queryset = Like.objects.all()

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)