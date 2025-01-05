from rest_framework import generics, permissions
from instapaws_api.permissions import IsOwnerOrReadOnly
from .models import Like
from .serializers import LikeSerializer

# Create your views here.
class LikeList(generics.ListCreateAPIView):
    """
    API view for listing and creating likes.

    - serializer_class: Uses LikeSerializer for Like objects.
    - permission_classes: Authenticated users can create; others have read-only access.
    - queryset: Retrieves all Like instances.

    Methods:
    - perform_create: Sets the owner field to the authenticated user when creating a like.
    """
    serializer_class = LikeSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    queryset = Like.objects.all()

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)