from django.db import models
from django.contrib.auth.models import User
from posts.models import Post

# Create your models here.
class Comment(models.Model):
    """
    Represents a comment made by a user on a post.

    Attributes:
        owner (User): The user who created the comment.
        post (Post): The post to which the comment belongs.
        comment_info (TextField): The content of the comment.
        created_at (DateTime): The timestamp when the comment was created.
        updated_at (DateTime): The timestamp when the comment was last updated.
    """
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    comment_info = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        """
        Defines default ordering of comments by most recent creation date.
        """
        ordering = ['-created_at']

    def __str__(self):
        """
        Returns a string representation of the comment's owner.
        """
        return f'{self.owner}'