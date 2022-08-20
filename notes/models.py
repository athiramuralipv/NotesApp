from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class UserProfile(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE,related_name="users")
    profile_pic=models.ImageField(upload_to="profilepics",null=True)
    email = models.EmailField(unique=True)

class Notes(models.Model):
    title=models.CharField(max_length=120)
    notes=models.CharField(max_length=500)
    image=models.ImageField(upload_to="notesimage",null=True)



