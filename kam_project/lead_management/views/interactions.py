from django.shortcuts import render, get_object_or_404, redirect
from django.forms import modelform_factory
from ..models import RestaurantLead, Interaction,Call
from django.contrib import messages
def interaction_form(request, lead_id):
    # Fetch the restaurant lead using the lead_id
    restaurant = get_object_or_404(RestaurantLead, id=lead_id)
    # Create a form for the Interaction model
    InteractionForm = modelform_factory(Interaction, fields=('type', 'notes', 'follow_up_required'))
    
    if request.method == 'POST':
        form = InteractionForm(request.POST)
        if form.is_valid():
            interaction = form.save(commit=False)
            interaction.restaurant = restaurant  # Associate the interaction with the restaurant
            interaction.save()
            print(f"Interaction ID: {interaction.id}")
            try:
                Call.objects.create(
                    lead=restaurant,
                    follow_up_required=interaction.follow_up_required,
                    notes=interaction.notes,
                    purpose=interaction.id,
                    res_name=restaurant.restaurant_name,
                )
            except Exception as e:
                print(f"Error saving Call: {e}")

            if interaction.follow_up_required:
                messages.success(request, "Follow-up call scheduled.")
            else:
                messages.success(request, "Interaction logged without follow-up.")

            return redirect('lead_detail', lead_id=restaurant.id)  # Redirect to the lead detail page
    else:
        form = InteractionForm()

    return render(request, 'lead_management/interaction_form.html', {'form': form, 'restaurant': restaurant})
