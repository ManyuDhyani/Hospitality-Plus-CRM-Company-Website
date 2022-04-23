from turtle import title
from django.db import models
from Activities.models import ActivitiesCategories

class Video(models.Model):
    home_Image = models.ImageField(upload_to ='uploads/images/%Y/%m/%d')
    video1 = models.FileField(upload_to ='upload/videos/%Y/%m/%d')
    video2 = models.FileField(upload_to ='upload/videos/%Y/%m/%d')
    video3 = models.FileField(upload_to ='upload/videos/%Y/%m/%d')
    video4 = models.FileField(upload_to ='upload/videos/%Y/%m/%d')

    class Meta:
        verbose_name_plural = "Home Videos"

class Services(models.Model):
    title1 = models.CharField(max_length=40)
    description1 = models.TextField(max_length=100)
    title2 = models.CharField(max_length=40)
    description2 = models.TextField(max_length=100)
    title3 = models.CharField(max_length=40)
    description3 = models.TextField(max_length=100)
    title4 = models.CharField(max_length=40)
    description4 = models.TextField(max_length=100)
    title5 = models.CharField(max_length=40)
    description5 = models.TextField(max_length=100)
    title6 = models.CharField(max_length=40)
    description6 = models.TextField(max_length=100)

    class Meta:
        verbose_name_plural = "Services"

class Gallery(models.Model):
    category = models.ForeignKey(ActivitiesCategories, on_delete=models.SET_NULL, null=True)
    thumbnail = models.ImageField(upload_to='upload/gallery/%Y/%m/%d')
    recommended = models.BooleanField(null=True, blank=True, default=False)
    location = models.CharField(max_length=40)
