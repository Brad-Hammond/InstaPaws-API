from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Follower(models.Model):
    """
    Represents a follower relationship between users.

    - 'owner': The user who is following another user, linked to the User model.
    - 'followed': The user being followed, also linked to the User model.
    - 'created_at': Timestamp when the follow relationship was created.
    """
    owner = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='following')
    followed = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='followed'
    )
    created_at = models.DateTimeField(auto_now_add=True)