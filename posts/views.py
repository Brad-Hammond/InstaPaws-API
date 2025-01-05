from rest_framework import generics, permissions, filters
from django.db.models import Count
from django_filters.rest_framework import DjangoFilterBackend
from instapaws_api.permissions import IsOwnerOrReadOnly
from .models import Post
from .serializers import PostSerializer

# Create your views here.
class PostList(generics.ListCreateAPIView):

    serializer_class = PostSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    queryset = Post.objects.annotate(
        likes_total=Count('likes', distinct=True),
        comments_total=Count('comment', distinct=True)
    ).order_by('-created_at')
    filter_backends = [
        filters.OrderingFilter,
        filters.SearchFilter,
        DjangoFilterBackend,
    ]
    filterset_fields = [
        'owner__profile',
        'tags',
        'likes__owner__profile',
        'owner__followed__owner__profile',
    ]
    search_fields = [
        'title',
        'tags',
        'owner__username'
    ]
    ordering_fields = [
        'comments_total',
        'likes_total',
        'likes__created_at',
    ]

    def perform_create(self, serializer):
 
        serializer.save(owner=self.request.user)