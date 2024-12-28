from django.db import models
from django.utils.timezone import now
from .restaurant import RestaurantLead
class Call(models.Model):
    lead = models.ForeignKey('RestaurantLead', on_delete=models.CASCADE, related_name='calls')
    follow_up_required = models.BooleanField(default=False)
    purpose = models.IntegerField(blank=True, null=True)
    notes = models.TextField(blank=True, null=True)  # Optional notes
    contact_person = models.CharField(max_length=100,default='xyz')
    res_name=models.CharField(max_length=100,default='xyz')
    def __str__(self):
        return f"{self.lead.restaurant_name} - {self.contact_person}"
