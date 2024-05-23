from django.db import models
from django.utils import timezone

# Create your models here.

class ALL_CHAI(models.Model):

    CHOICES = [
        ('MLT' , 'masala'),
        ('PLT' , 'plain'),
        ('ELT' , 'elaichi'),
    ]


    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='batman/')
    date_added = models.DateTimeField(default=timezone.now)
    type = models.CharField(max_length=3 , choices=CHOICES)

    def __str__(self):
        return self.name