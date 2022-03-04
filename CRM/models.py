from asyncio import events
from django.db import models
from django.contrib.auth import get_user_model
from ckeditor_uploader.fields import RichTextUploadingField
from simple_history.models import HistoricalRecords

User = get_user_model()

class Agent(models.Model):
    agent = models.OneToOneField(User, on_delete=models.CASCADE)
    profile_picture = models.ImageField(null=True, blank=True, upload_to="profile_pictures/agents/")

    class Meta:
        verbose_name_plural = 'Agents'

    def __str__(self):
        return self.agent.username


class Event(models.Model):
    title = models.CharField(max_length=100)

    class Meta:
        verbose_name_plural = 'Events'

    def __str__(self):
        return self.title

class Category(models.Model):
    title = models.CharField(max_length=100)

    class Meta:
        verbose_name_plural = 'Categories'

    def __str__(self):
        return self.title


CUSTOMER_STATUS_CHOICES = (
        ('Lead', 'Lead'),
        ('Customer', 'Customer')
    )

GENDER_CHOICES = (
        ('Male', 'Male'),
        ('Female', 'Female'),
        ('Rather not say', 'Rather not say')
    )

class CustomerChangeUser(models.Model):
    user_id = models.ForeignKey('auth.User', on_delete=models.CASCADE)

class Customer(models.Model):
    first_name = models.CharField(max_length=40)
    middle_name = models.CharField(max_length=40, null=True, blank=True)
    last_name = models.CharField(max_length=40)
    age = models.IntegerField(default=0, null=True, blank=True)
    gender = models.CharField(max_length=20, choices=GENDER_CHOICES)
    number_of_calls = models.IntegerField(default=0, null=True, blank=True)
    category_attended = models.ManyToManyField(Category, blank=True)
    events = models.ForeignKey(Event, null=True, blank=True, on_delete=models.SET_NULL)
    phone_number = models.CharField(max_length=20)
    email = models.EmailField(null=True, blank=True)
    status = models.CharField(max_length=10, choices=CUSTOMER_STATUS_CHOICES, default='Customer')
    converted_date = models.CharField(max_length=40, null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    profile_picture = models.ImageField(null=True, blank=True, upload_to="profile_pictures/")
    customer_details = RichTextUploadingField(null=True, blank=True)
    date_added = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)
    agent = models.ForeignKey(Agent, related_name="Agent", null=True, blank=True, on_delete=models.SET_NULL)
    changed_by = models.ForeignKey(CustomerChangeUser, on_delete=models.SET_NULL, null=True, blank=True)
    history = HistoricalRecords()

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

class Newsletter(models.Model):
    email = models.EmailField()
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.email

    class Meta:
        verbose_name_plural = "Newsletters Emails"