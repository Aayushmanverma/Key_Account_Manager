from django.contrib import admin
from .models import RestaurantLead, Contact
from .models import Interaction,Call

@admin.register(RestaurantLead)
class RestaurantLeadAdmin(admin.ModelAdmin):
    list_display = ('restaurant_name', 'status', 'assigned_kam')
    search_fields = ('restaurant_name', 'address')
    list_filter = ('status',)

@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ('name', 'role', 'phone_number', 'email', 'restaurant')
    search_fields = ('name', 'email', 'restaurant__restaurant_name')
    list_filter = ('role',)

@admin.register(Interaction)
class InteractionAdmin(admin.ModelAdmin):
    list_display = ('restaurant', 'type', 'date', 'follow_up_required')
    list_filter = ('type', 'follow_up_required')
    search_fields = ('restaurant__restaurant_name', 'notes')

@admin.register(Call)
class CallAdmin(admin.ModelAdmin):
    list_display = ('lead', 'follow_up_required')