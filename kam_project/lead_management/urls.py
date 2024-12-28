from django.urls import path
from .views.dashboard import dashboard
from .views.leads import lead_list, lead_detail, lead_form
from .views.contacts import contact_form, edit_contact
from .views.interactions import interaction_form
from .views.leads import delete_lead
from .views.leads import pending_calls_view,mark_call_completed,edit_call
urlpatterns = [
    # Dashboard URL
    path('', dashboard, name='dashboard'),

    # Lead-related URLs
    path('leads/', lead_list, name='lead_list'),  # List all leads
    path('leads/add/', lead_form, name='add_lead'),  # Add a new lead
    path('leads/<int:lead_id>/', lead_detail, name='lead_detail'),  # View lead details
    path('leads/<int:lead_id>/edit/', lead_form, name='edit_lead'),  # Edit a lead

    # Contact-related URL
    path('leads/<int:lead_id>/add-contact/', contact_form, name='add_contact'),  # Add a contact to a lead

    # Interaction-related URL
    path('leads/<int:lead_id>/log-interaction/', interaction_form, name='log_interaction'),  # Log an interaction for a lead
    # edit_contact-related URL
    path('leads/<int:lead_id>/edit-contact/<int:contact_id>/', edit_contact, name='edit_contact'),
    # delete_lead -related URL
    path('leads/<int:lead_id>/delete/', delete_lead, name='delete_lead'),
    # Other URL patterns
    path('pending-calls/', pending_calls_view, name='pending_calls'),

    path('calls/<int:purpose>/completed/', mark_call_completed, name='mark_call_completed'),
]
