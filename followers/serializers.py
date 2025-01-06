from django.db import IntegrityError
from rest_framework import serializers
from .models import Follower

class FollowerSerializer(serializers.ModelSerializer):
    """
    FollowerSerializer:
    - Serializes the Follower model to handle JSON data exchange.
    - Includes fields to represent the owner (user who follows) and 
      the followed user, along with additional metadata.
    """
    owner = serializers.ReadOnlyField(source='owner.username')
    followed_username = serializers.ReadOnlyField(source='followed.username')

    class Meta:
        """
        Meta:
        - Specifies the model associated with this serializer.
        - Defines the fields to be serialized.
        """
        model = Follower
        fields = ['id', 'owner', 'created_at', 'followed_username', 'followed']

    def create(self, validated_data):
        """
        Custom create method:
        - Attempts to create a new Follower instance with the validated data.
        - Handles the IntegrityError if the user tries to follow the same 
          person more than once, raising a validation error instead.
        """
        try:
            return super().create(validated_data)
        except IntegrityError:
            raise serializers.ValidationError(
                {'detail': 'duplicated follow, one follow per user'})
