from django.db import models
from django.db.models.signals import post_save
from django.contrib.auth.models import User


# Create your models here.
class Profile(models.Model):
    '''
    Represents a user's profile in the application.

    Attributes:
        owner (User): A one-to-one relationship with the User model.
        created_at (DateTime): Timestamp for when the profile was created.
        updated_at (DateTime): Timestamp for when the profile was last updated.
        name (str): Optional name field for the profile.
        content (str): Optional bio or description field for the profile.
        image (ImageField): Profile image, with a default placeholder
        if not provided.
    '''
    owner = models.OneToOneField(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    name = models.CharField(max_length=255, blank=True)
    content = models.TextField(blank=True)
    image = models.ImageField(
        upload_to='images/', default='../default_profile_wxgp9p'
    )

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return f"{self.owner}'s profile"


def create_profile(sender, instance, created, **kwargs):
    '''
    Signal function to automatically create a Profile instance
    when a new User is created.

    Args:
        sender: The model class sending the signal (User in this case).
        instance: The User instance being created or saved.
        created (bool): Indicates whether the User instance was newly created.
        **kwargs: Additional keyword arguments.
    '''

    if created:
        Profile.objects.create(owner=instance)


post_save.connect(create_profile, sender=User)
