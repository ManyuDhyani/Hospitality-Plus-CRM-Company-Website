from django.db import models
from django.db.models.signals import pre_save
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
    thumbnail = models.ImageField(upload_to='upload/treks')
    recommended = models.BooleanField(null=True, blank=True, default=False)
    altitude = models.CharField(max_length=20)
    duration_days = models.CharField(max_length=20)
    difficulty = models.CharField(max_length=20)
    location = models.CharField(max_length=40)
    distance = models.CharField(max_length=20)
    price = models.CharField(max_length=20)
    description = models.TextField(max_length=250)
    category = models.ForeignKey(ActivitiesCategories, on_delete=models.SET_NULL, null=True)

    class Meta:
        verbose_name_plural = 'Activities'

    def __str__(self):
        return self.title

def slug_generator(sender, instance, *args, **kwargs):
    if not instance.slug:
        instance.slug = unique_slug_generator_title(instance)
               
pre_save.connect(slug_generator, sender=Activities)