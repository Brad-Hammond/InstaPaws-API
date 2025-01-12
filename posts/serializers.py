from rest_framework import serializers
from likes.models import Like
from .models import Post


class PostSerializer(serializers.ModelSerializer):
    """
    Serializer for the Post model.
    - Converts Post objects into JSON format for API responses.
    - Handles validation and ensures data integrity for posts.
    """
    owner = serializers.ReadOnlyField(source='owner.username')
    is_owner = serializers.SerializerMethodField()
    like_id = serializers.SerializerMethodField()
    likes_total = serializers.ReadOnlyField()
    comments_total = serializers.ReadOnlyField()
    profile_id = serializers.ReadOnlyField(source='owner.profile.id')
    profile_image = serializers.ReadOnlyField(source='owner.profile.image.url')

    def validate_image(self, value):
        """
        Validates the uploaded image for file size, height, and width.
        - Ensures the file size does not exceed 2MB.
        - Checks that the image height is no greater than 4096 pixels.
        - Verifies that the image width is no greater than 4096 pixels.
        - Raises a ValidationError if any of these conditions are violated.
        - Returns the image if all validations pass.
        """
        if value.size > 2 * 1024 * 1024:
            raise serializers.ValidationError('Image size larger than 2MB!')
        if value.image.height > 4096:
            raise serializers.ValidationError(
                'Image height larger than 4096px!'
            )
        if value.image.width > 4096:
            raise serializers.ValidationError(
                'Image width larger than 4096px!'
            )
        return value

    def get_is_owner(self, obj):
        """
        Checks ownership of the post.
        - Retrieves the current user from the request context.
        - Compares the authenticated user with the owner of the post.
        - Returns True if the user is the owner, otherwise False.
        """
        request = self.context['request']
        return request.user == obj.owner

    def get_like_id(self, obj):
        """
        Retrieves the ID of the like relationship for the current
        user and post.
        - If the authenticated user has liked the post, return the like ID.
        - If no like exists or the user is not authenticated, return None.
        """
        user = self.context['request'].user
        if user.is_authenticated:
            like = Like.objects.filter(
                owner=user, post=obj
            ).first()
            return like.id if like else None
        return None

    class Meta:
        """
        Metadata for the PostSerializer.
        - Specifies the Post model as the source.
        - Defines the fields to include in the serialized output.
        """
        model = Post
        fields = ['id', 'owner', 'is_owner', 'profile_id', 'profile_image',
                  'created_at', 'updated_at', 'title', 'content', 'image',
                  'like_id', 'likes_total', 'comments_total', 'tags',
                  ]
