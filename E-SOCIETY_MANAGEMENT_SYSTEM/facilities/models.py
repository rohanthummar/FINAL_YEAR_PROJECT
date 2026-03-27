from django.db import models
from users.models import User


class Facility(models.Model):

    name = models.CharField(max_length=100)

    description = models.TextField()

    def __str__(self):
        return self.name


class Booking(models.Model):

    STATUS_CHOICES = (
        ('pending', 'Pending'),
        ('approved', 'Approved'),
        ('rejected', 'Rejected'),
    )

    resident = models.ForeignKey(User, on_delete=models.CASCADE)

    facility = models.ForeignKey(Facility, on_delete=models.CASCADE)

    booking_date = models.DateField()

    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='pending')

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.resident.username} - {self.facility.name}"