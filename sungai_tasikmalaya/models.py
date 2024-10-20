from django.db import models
from django.contrib.auth.models import User

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True, blank=True)
    alamat = models.CharField(max_length=255)
    tanggal_lahir = models.DateField(null=True, blank=True) 
    no_hp = models.CharField(max_length=15, null=True, blank=True) 
    instagram = models.CharField(max_length=50, blank=True, null=True)
    tiktok = models.CharField(max_length=50, blank=True, null=True)
    x = models.CharField(max_length=50, blank=True, null=True)

    def __str__(self):
        return self.user.username if self.user else 'No User'
