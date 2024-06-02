from django.db import models

# Create your models here.

class Person(models.Model):
    GENDER_CHOICES = [
        ('M', 'Male'),
        ('F', 'Female'),
        ('O', 'Other'),
    ]
    name = models.CharField(max_length=100)
    description = models.TextField()
    gender = models.CharField(max_length=10, choices=GENDER_CHOICES, default='M')
    date_of_birth = models.DateField(null=True, blank=True)