from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Follower(models.Model):
    """
    Represents a follower relationship between users.

    - 'owner': The user who is following another user, linked to
    the User model.
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

    class Meta:
        """
        Metadata for the Follower model.

        - 'ordering': Orders follower records by creation time in
           descending order.
        - 'unique_together': Ensures that each owner can only follow a
           specific user once.
        """
        ordering = ['-created_at']
        unique_together = ['owner', 'followed']

    def __str__(self):
        '''
        Returns a string representation of the follower relationship
        showing the follower and the followed user.
        '''
        return f'{self.owner} {self.followed}'
