from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Follower(models.Model):

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