from django.db.models import Count
from rest_framework import generics, filters
from django_filters.rest_framework import DjangoFilterBackend
from drf_api.permissions import IsOwnerOrReadOnly
from .models import Profile
from .serializers import ProfileSerializer


# Create your views here.
class ProfileList(generics.ListAPIView):
    """
ProfileList View:
- Provides a list of profiles with annotated fields:
  - followers_total: Total number of followers of the profile owner.
  - following_total: Total number of users the profile owner is following.
  - posts_total: Total number of posts created by the profile owner.
- Allows filtering profiles based on:
  - Profiles the owner is following.
  - Profiles that are following the owner.
- Supports ordering by:
  - Total posts, followers, followings, and creation dates of relationships.
- Utilizes Django REST Framework's generic ListAPIView.
"""
    queryset = Profile.objects.annotate(
        followers_total=Count('owner__followed', distinct=True),
        following_total=Count('owner__following', distinct=True),
        posts_total=Count('owner__post', distinct=True)
    ).order_by('-created_at')
    serializer_class = ProfileSerializer
    filter_backends = [
        filters.OrderingFilter,
        DjangoFilterBackend,
    ]
    filterset_fields = [

        # displays profile results that are following
        'owner__following__followed__profile',
        # displays profile results that are followed
        'owner__followed__owner__profile',
    ]
    ordering_fields = [
        'posts_total',
        'owner__following__created_at',
        'owner__followed__created_at',
        'followers_total',
        'following_total',
    ]


class ProfileDetail(generics.RetrieveUpdateAPIView):
    """
ProfileDetail View:
- Handles the retrieval and updating of a single profile instance.
- Permissions:
  - Uses IsOwnerOrReadOnly to ensure only the profile owner can update
    their profile,
    while others can only view it.
- Queryset:
  - Annotates the profile with additional information:
    - followers_total: Total number of users following the profile owner.
    - following_total: Total number of users the profile owner is following.
    - posts_total: Total number of posts created by the profile owner.
  - Orders the profiles by creation date in descending order.
- Serializer:
  - Utilizes ProfileSerializer to serialize the profile data for API responses
    and handle updates from API requests.
"""
    permission_classes = [IsOwnerOrReadOnly]
    queryset = Profile.objects.annotate(
        followers_total=Count('owner__followed', distinct=True),
        following_total=Count('owner__following', distinct=True),
        posts_total=Count('owner__post', distinct=True)
    ).order_by('-created_at')
    serializer_class = ProfileSerializer
