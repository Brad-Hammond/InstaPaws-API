from django.db import IntegrityError
from rest_framework import serializers
from .models import Like


class LikeSerializer(serializers.ModelSerializer):
    """
    Serializer for the Like model, handling the conversion
    of Like instances to and from JSON format.
    """
    owner = serializers.ReadOnlyField(source='owner.username')

    class Meta:
        """
        Metadata for LikeSerializer.
        - model: Specifies the Like model.
        - fields: Includes 'id', 'owner' (username of the like creator),
          'post' (liked post ID), and 'created_at' (creation timestamp).
        """
        model = Like
        fields = ['id', 'owner', 'post', 'created_at']

    def create(self, validated_data):
        """
        Handles IntegrityError to prevent a user from liking the
        same post multiple times.
        Raises a ValidationError with a descriptive message if
        duplication occurs.
        """
        try:
            return super().create(validated_data)
        except IntegrityError:
            raise serializers.ValidationError({
                'detail': 'duplicated like, error'
            })
