from django.db import models
from django.contrib.auth.models import User
from posts.models import Post

# Create your models here.
class Like(models.Model):
    """
    Represents a 'like' on a post in the application.

    Fields:
    - owner: The user who liked the post, linked as a foreign key to the User model.
             If the user is deleted, their likes will also be removed (on_delete=models.CASCADE).
    - post: The post that has been liked, linked as a foreign key to the Post model.
            Includes a 'related_name' attribute ('likes') to enable reverse access from a Post instance.
    - created_at: A timestamp that indicates when the like was created, automatically set at the time of creation.
    """
    owner = models.ForeignKey(
        User,
        on_delete=models.CASCADE)
    post = models.ForeignKey(
        Post,
        on_delete=models.CASCADE,
        related_name='likes'
    )
    created_at = models.DateTimeField(auto_now_add=True)