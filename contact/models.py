from django.db import models
from django.utils import timezone

# Create your models here.


class Contact(models.Model):
    fist_name = models.CharField(max_length=40)
    last_name = models.CharField(max_length=40)
    phone = models.CharField(max_length=40)
    email = models.EmailField(max_length=255)
    created_date = models.DateTimeField(default=timezone.now)
    description = models.TextField(blank=True)
