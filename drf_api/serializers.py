from dj_rest_auth.serializers import UserDetailsSerializer
from rest_framework import serializers


class CurrentUserSerializer(UserDetailsSerializer):
    """
    CurrentUserSerializer:
    - Extends the `UserDetailsSerializer` from dj_rest_auth
      to include additional fields.
    - Adds fields to represent the user's profile information,
      specifically the profile ID
      and the URL of the profile image.
    """
    profile_id = serializers.ReadOnlyField(source='profile.id')
    profile_image = serializers.ReadOnlyField(source='profile.image.url')

    class Meta(UserDetailsSerializer.Meta):
        """
        Meta:
        - Extends the Meta class of the base `UserDetailsSerializer`.
        - Adds custom fields `profile_id` and `profile_image` to the
          serialized output
          while retaining all fields from the base serializer.
        """
        fields = UserDetailsSerializer.Meta.fields + (
            'profile_id', 'profile_image'
        )
