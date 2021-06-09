from django.db import models
from django.conf import settings

# Create your models here.


class Profile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL,on_delete=models.CASCADE)
    date_of_birth = models.DateField(blank=True, null=True)
    photo = models.ImageField(upload_to='users/%Y/%m/%d/',blank=True)
    Post = models.CharField(blank=False,null=True,max_length=100)

    def __str__(self):
        return f'Profile for user {self.user.username}'


class CriminalProfile(models.Model):
    Name = models.CharField(max_length=100)
    date_of_birth = models.DateField(blank=True, null=True)
    photo = models.ImageField(upload_to='users/%Y/%m/%d/',blank=True)
    cases = models.CharField(blank=False,max_length=6500)

    def __str__(self):
        return f'Profile for user {self.Name}'

   
