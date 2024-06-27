from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class UserProfile(models.Model):
    user=models.OneToOneField(User,related_name="userprofile",on_delete=models.CASCADE)
    is_vendor=models.BooleanField(default=False)
    vendor_name=models.CharField(max_length=15,null=True)
    address=models.CharField(max_length=100,null=True,blank=True)
    phone=models.CharField(max_length=10,blank=True,null=True)
    email=models.EmailField(null=True,blank=True)
    def __str__(self):
        return self.user.username