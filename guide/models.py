from django.db import models
from django.contrib.auth.models import User
from django.core.files.storage import FileSystemStorage
from django.utils import timezone
# Create your models here.
class Profile(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    phone=models.IntegerField()
    city=models.CharField(max_length=25)
    class Meta:
        verbose_name_plural = "Profiles"
class Audio(models.Model):
    userId=models.ForeignKey(User,on_delete=models.CASCADE)
    language=models.CharField(max_length=20)
    file=models.FileField(upload_to='files/')
    city=models.CharField(max_length=25)
    priority=models.BooleanField(default=False)

class Place(models.Model):
    name=models.CharField(max_length=30)
    city=models.CharField(max_length=25)
    lon=models.DecimalField(max_digits=22, decimal_places=16)
    lat=models.DecimalField(max_digits=22, decimal_places=16)
    pic=models.FileField(upload_to='pictures/',blank=True,null=True)

class AudioRating(models.Model):
    audioId=models.ForeignKey(Audio,on_delete=models.CASCADE)
    comment=models.TextField(null=True,blank=True)
    rating=models.IntegerField(null=True,blank=True)
    user=models.ForeignKey(User,on_delete=models.CASCADE)

class PlaceRating(models.Model):
    placeId=models.ForeignKey(Place,on_delete=models.CASCADE)
    comment=models.TextField(null=True,blank=True)
    rating=models.IntegerField(null=True,blank=True)
    user=models.ForeignKey(User,on_delete=models.CASCADE)
