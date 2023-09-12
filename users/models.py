from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    img = models.ImageField('User`s photo', default='default.png', upload_to='user_images')

    def __str__(self):
        return f'User`s profile {self.user.username}'
    class Meta:
        verbose_name = 'Profile'
        verbose_name_plural = 'Profiles'
