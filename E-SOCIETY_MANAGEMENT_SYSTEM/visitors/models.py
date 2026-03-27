from django.db import models
from users.models import User


class Visitor(models.Model):

    STATUS_CHOICES = (
        ('pending', 'Pending'),
        ('approved', 'Approved'),
        ('rejected', 'Rejected'),
    )

    visitor_name = models.CharField(max_length=100)

    phone = models.CharField(max_length=15)

    flat_number = models.CharField(max_length=10)

    purpose = models.CharField(max_length=200)

    resident = models.ForeignKey(User, on_delete=models.CASCADE)

    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='pending')

    visit_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.visitor_name