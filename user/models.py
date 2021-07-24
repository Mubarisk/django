from django.contrib.auth.models import User
from django.db import models


# Create your models here.
class UserProfile(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    image = models.ImageField(null=True, blank=True, upload_to='images/')
    phone = models.IntegerField()
    like = models.IntegerField(null=True, blank=True, default=0)

    def __str__(self):
        return self.user


class Director(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    position = models.CharField(max_length=25, default='user', blank=True, null=True)

    def __str__(self):
        return self.position


class Requests(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    userid = models.IntegerField()
    status = models.CharField(null=True, blank=True, max_length=25)

    def __str__(self):
        return self.status
