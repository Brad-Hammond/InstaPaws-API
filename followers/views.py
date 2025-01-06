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

    serializer_class = FollowerSerializer
    permission_classes = [IsOwnerOrReadOnly]
    queryset = Follower.objects.all()