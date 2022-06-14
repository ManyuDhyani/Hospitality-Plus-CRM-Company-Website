from django.db import models
from django.db.models.signals import pre_save
from django.urls import reverse
from .utils import unique_slug_generator_title
from ckeditor_uploader.fields import RichTextUploadingField

class ActivitiesCategories(models.Model):
    category = models.CharField(max_length=40)

    class Meta:
        verbose_name_plural = 'Activities Categories'

    def __str__(self):
        return self.category


class Activities(models.Model):
    title = models.CharField(max_length=150)
    slug = models.SlugField(max_length=250, null=True, blank=True)
    thumbnail = models.ImageField(upload_to='upload/activities')
    recommended = models.BooleanField(null=True, blank=True, default=False)
    altitude = models.CharField(max_length=20, null=True, blank=True)
    duration_days = models.CharField(max_length=20, null=True, blank=True)
    difficulty = models.CharField(max_length=20, null=True, blank=True)
    location = models.CharField(max_length=40)
    distance = models.CharField(max_length=20, null=True, blank=True)
    old_price = models.CharField(max_length=20, null=True, blank=True)
    price = models.CharField(max_length=20)
    description = models.TextField(max_length=250)
    category = models.ForeignKey(ActivitiesCategories, on_delete=models.SET_NULL, null=True)
    content = RichTextUploadingField(null=True, blank=True)
    thumbnail = models.ImageField(upload_to='uplo ad/activities', default="images/whiteBG.jpg")
    thumbnail_2 = models.ImageField(upload_to='upload/activities', default="images/whiteBG.jpg")
    thumbnail_3 = models.ImageField(upload_to='upload/activities', default="images/whiteBG.jpg")
    thumbnail_4 = models.ImageField(upload_to='upload/activities', default="images/whiteBG.jpg")
    banner_quote = models.CharField(max_length=160, null=True, blank=True)

    class Meta:
        verbose_name_plural = 'Activities'

    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse('Activities:activity-detail', kwargs={
            'slug': self.slug
        })

def slug_generator(sender, instance, *args, **kwargs):
    if not instance.slug:
        instance.slug = unique_slug_generator_title(instance)
               
pre_save.connect(slug_generator, sender=Activities)