from django.db import models

class RestaurantLead(models.Model):
    STATUS_CHOICES = [
        ('new', 'New'),
        ('active', 'Active'),
        ('inactive', 'Inactive'),
    ]

    restaurant_name = models.CharField(max_length=255)
    address = models.TextField()
    contact_number = models.CharField(max_length=15)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='new')
    assigned_kam = models.CharField(max_length=255)

    def __str__(self):
        return self.restaurant_name
