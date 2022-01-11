from django.db import models

# Create your models here.

class Round2database(models.Model): 
    name = models.CharField(max_length=20, default=False, blank=True)
    roll = models.CharField(max_length=9, default=False, blank=True)
    number = models.CharField(max_length=14, default=False, blank=True)
    email = models.EmailField(default=False, blank=True)
    slot = models.CharField(max_length=15, default=False, blank=True)
    interviewer = models.CharField(max_length=30, default=False, blank=True)
    taken = models.CharField(max_length=10, blank=True, default=False)
    selected = models.CharField(max_length=10, blank=True, default=False)

    def __str__(self):
        return self.roll