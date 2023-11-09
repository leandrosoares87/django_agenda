from django.db import models
from django.utils import timezone


class Contact(models.Model):
    fist_name = models.CharField(max_length=40)
    last_name = models.CharField(max_length=40)
    phone = models.CharField(max_length=40)
    email = models.EmailField(max_length=255, blank=True)
    created_date = models.DateTimeField(default=timezone.now)
    description = models.TextField(blank=True)
    show = models.BooleanField(default=True)
    picture = models.ImageField(blank=True, upload_to='picture/%Y/%m/')

    def __str__(self) -> str:
        return f'{self.fist_name} {self.last_name}'
