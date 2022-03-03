from django.urls import reverse
from django import template

register = template.Library()

@register.filter
def rev(value):
    return reverse(value)