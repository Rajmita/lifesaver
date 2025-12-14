# Creating models here.
from django.db import models

class BloodPost(models.Model):
    BLOOD_TYPES = [
        ('A+', 'A+'), ('A-', 'A-'),
        ('B+', 'B+'), ('B-', 'B-'),
        ('O+', 'O+'), ('O-', 'O-'),
        ('AB+', 'AB+'), ('AB-', 'AB-'),
    ]

    name = models.CharField(max_length=100)
    blood_type = models.CharField(max_length=5, choices=BLOOD_TYPES)
    city = models.CharField(max_length=100)
    contact = models.CharField(max_length=20)
    message = models.TextField(blank=True)
    urgent = models.BooleanField(default=False)  # NEW FIELD
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} - {self.blood_type}"


