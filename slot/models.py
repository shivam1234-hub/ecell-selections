from django.db import models
from datetime import datetime, date

from django.db.models.expressions import F

# Create your models here.

class database(models.Model):
    name=models.CharField(max_length=50, blank=True, default=True)
    roll = models.CharField(max_length=9, default=False, blank=True)
    file = models.FileField(upload_to ='uploads/')
    slot = models.CharField(max_length=15, default=False, blank=True)
    datestamp = models.DateField(auto_now_add=True, null=True, blank=True)
    timestamp = models.TimeField(auto_now_add=True, null=True, blank=True)

    def __str__(self):
        return self.roll