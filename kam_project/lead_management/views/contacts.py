from django.shortcuts import render, get_object_or_404, redirect
from django.forms import modelform_factory
from ..models import Contact
from django.shortcuts import render, get_object_or_404, redirect
from django.forms import modelform_factory
from ..models import RestaurantLead, Contact

def contact_form(request, lead_id):
    # Fetch the restaurant lead using the lead_id
    restaurant = get_object_or_404(RestaurantLead, id=lead_id)
    # Create a form for the Contact model
    ContactForm = modelform_factory(Contact, fields=('name', 'role', 'phone_number', 'email'))
    
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            contact = form.save(commit=False)
            contact.restaurant = restaurant  # Associate the contact with the restaurant
            contact.save()
            return redirect('lead_detail', lead_id=restaurant.id)  # Redirect to the lead detail page
    else:
        form = ContactForm()

    return render(request, 'lead_management/contact_form.html', {'form': form, 'restaurant': restaurant})


def edit_contact(request, lead_id, contact_id):
    # Fetch the contact to be edited
    contact = get_object_or_404(Contact, id=contact_id, restaurant__id=lead_id)
    
    # Create a modelform for the Contact model
    ContactForm = modelform_factory(Contact, fields=('name', 'role', 'phone_number', 'email'))
    
    if request.method == 'POST':
        form = ContactForm(request.POST, instance=contact)
        if form.is_valid():
            form.save()
            return redirect('lead_detail', lead_id=lead_id)  # Redirect to the lead detail page after saving
    else:
        form = ContactForm(instance=contact)  # Pre-fill the form with existing data

    return render(request, 'lead_management/contact_form.html', {
        'form': form,
        'restaurant_name': contact.restaurant.restaurant_name,
        'edit_mode': True  # Add a flag to indicate edit mode in the template
    })
