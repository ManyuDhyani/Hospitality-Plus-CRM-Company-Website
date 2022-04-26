from django.db import models
from Activities.models import ActivitiesCategories

class Video(models.Model):
    header_Image = models.ImageField(upload_to ='uploads/images/%Y/%m/%d')
    video1 = models.FileField(upload_to ='upload/videos/%Y/%m/%d')
    video2 = models.FileField(upload_to ='upload/videos/%Y/%m/%d')
    video3 = models.FileField(upload_to ='upload/videos/%Y/%m/%d')
    video4 = models.FileField(upload_to ='upload/videos/%Y/%m/%d')
    footer_Image = models.ImageField(upload_to ='uploads/images/%Y/%m/%d')

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
    image = models.ImageField(upload_to='upload/gallery/%Y/%m/%d')
    recommended = models.BooleanField(null=True, blank=True, default=False)
    location = models.CharField(max_length=40)

    class Meta:
        verbose_name_plural = "Gallery"

class Testimonials(models.Model):
    name=models.CharField(max_length=20)
    profile_picture = models.ImageField(upload_to='upload/profilePicture/%Y/%m/%d')
    coming_from = models.CharField(max_length=40)
    review = models.TextField(max_length=150)
    recommended = models.BooleanField(null=True, blank=True, default=False)

    class Meta:
        verbose_name_plural = "Testimonials"

class ContactDetails(models.Model):
    office_location = models.CharField(max_length=40)
    office_phone = models.CharField(max_length=30)
    office_email = models.EmailField()
    office_timings=models.CharField(max_length=20)

    class Meta:
        verbose_name_plural = "ContactDetails"

class Quotes(models.Model):
    header=models.CharField(max_length=160)
    about_us=models.CharField(max_length=160)
    testimonials=models.CharField(max_length=250)
    bottom_banner=models.CharField(max_length=160)
    footer=models.CharField(max_length=80)

    class Meta:
        verbose_name_plural = "Quotes"

class Blogs(models.Model):
    title = models.CharField(max_length=100)
    overview = models.TextField(null=True, blank=True)
    timestamp = models.DateTimeField()
    author = models.CharField(max_length=40)
    thumbnail = models.URLField(max_length=250)
    blog_url = models.URLField(max_length=250, default="https://www.hashstrix.com/tag/traveloft/")
    recommended = models.BooleanField(null=True, blank=True, default=False)

    class Meta:
        verbose_name_plural = "Blogs"

    def __str__(self):
        return self.title