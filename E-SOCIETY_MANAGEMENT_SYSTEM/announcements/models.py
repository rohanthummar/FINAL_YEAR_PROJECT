from django.db import models
from users.models import User


class Announcement(models.Model):

    title = models.CharField(max_length=200)

    message = models.TextField()

    created_by = models.ForeignKey(User, on_delete=models.CASCADE)

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title