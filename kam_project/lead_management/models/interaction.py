from django.db import models
from .restaurant import RestaurantLead

class Interaction(models.Model):
    TYPE_CHOICES = [
        ('call', 'Call'),
        ('visit', 'Visit'),
        ('order', 'Order'),
    ]

    restaurant = models.ForeignKey(
        RestaurantLead, 
        on_delete=models.CASCADE, 
        related_name='interactions'
    )
    date = models.DateField(auto_now_add=True)  # Automatically sets the date when the interaction is created
    type = models.CharField(max_length=10, choices=TYPE_CHOICES)
    notes = models.TextField(blank=True, null=True)  # Optional notes
    follow_up_required = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.get_type_display()} - {self.restaurant.restaurant_name} on {self.date}"
