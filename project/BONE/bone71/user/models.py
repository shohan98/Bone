from django.db import models
from Boneadmin.models import User
# Create your models here.

class BoneUser(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    user_ip = models.CharField(max_length=50, blank=True)

    def __str__(self):
        return self.user.username