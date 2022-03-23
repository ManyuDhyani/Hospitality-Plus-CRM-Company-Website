from django.db import models

class ActivitiesCategories(models.Model):
    category = models.CharField(max_length=40)

    class Meta:
        verbose_name_plural = 'Activities Categories'

    def __str__(self):
        return self.category


class Activities(models.Model):
    name = models.CharField(max_length=40)
    slug = models.SlugField(max_length=100, null=True, blank=True)
    thumbnail = models.ImageField(upload_to='upload/treks')
    recommended = models.BooleanField(null=True, blank=True, default=False)
    altitude = models.CharField(max_length=20)
    duration_days = models.CharField(max_length=20)
    difficulty = models.CharField(max_length=20)
    district = models.CharField(max_length=40)
    distance = models.CharField(max_length=20)
    price = models.CharField(max_length=20)
    description = models.TextField(max_length=150)
    category = models.ForeignKey(ActivitiesCategories, on_delete=models.SET_NULL, null=True)