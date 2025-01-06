from rest_framework import generics, permissions
from instapaws_api.permissions import IsOwnerOrReadOnly
from .models import Follower
from .serializers import FollowerSerializer

# Create your views here.
class FollowerList(generics.ListCreateAPIView):
    """
    API view for listing followers and creating follow relationships.

    - Lists all followers for a user.
    - Allows authenticated users to create new follow relationships.
    """
    serializer_class = FollowerSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    queryset = Follower.objects.all()

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

class FollowerDetail(generics.RetrieveUpdateDestroyAPIView):
    """
    API view for retrieving, updating, or deleting a specific follower relationship.

    - Allows retrieving details of a follower by ID.
    - Enables the owner to update or delete the follower relationship.
    """
    serializer_class = FollowerSerializer
    permission_classes = [IsOwnerOrReadOnly]
    queryset = Follower.objects.all()