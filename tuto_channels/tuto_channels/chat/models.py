from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Chat(models.Model):
    """Model definition for Chat."""

    # TODO: Define fields here
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user', null=True)
    message = models.TextField()
    statut = models.BooleanField(default=False)
    date_add = models.DateTimeField(auto_now_add=True)
    date_up = models.DateTimeField(auto_now=False,)

    class Meta:
        """Meta definition for Chat."""

        verbose_name = 'Chat'
        verbose_name_plural = 'Chats'


