from django.db import models
from users.models import User


class MaintenanceBill(models.Model):

    STATUS_CHOICES = (
        ('unpaid', 'Unpaid'),
        ('paid', 'Paid'),
    )

    resident = models.ForeignKey(
    User,
    on_delete=models.CASCADE,
    limit_choices_to={'role': 'resident'}
)

    month = models.CharField(max_length=20)

    amount = models.DecimalField(max_digits=8, decimal_places=2)

    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='unpaid')

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.resident.username} - {self.month}"