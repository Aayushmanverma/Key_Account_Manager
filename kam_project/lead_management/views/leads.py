from django.shortcuts import render, get_object_or_404, redirect
from django.forms import modelform_factory
from ..models import RestaurantLead,Call,Interaction
from django.contrib import messages
import logging
def lead_list(request):
    leads = RestaurantLead.objects.all()
    return render(request, 'lead_management/lead_list.html', {'leads': leads})

def lead_detail(request, lead_id):
    lead = get_object_or_404(RestaurantLead, id=lead_id)
    contacts = lead.contacts.all()
    interactions = lead.interactions.all()
    return render(request, 'lead_management/lead_detail.html', {
        'lead': lead,
        'contacts': contacts,
        'interactions': interactions,
    })

def lead_form(request, lead_id=None):
    LeadForm = modelform_factory(RestaurantLead, exclude=[])
    if lead_id:
        lead = get_object_or_404(RestaurantLead, id=lead_id)
        lead_form_title = "Edit Lead"
    else:
        lead = None
        lead_form_title = "Add Lead"

    if request.method == 'POST':
        form = LeadForm(request.POST, instance=lead)
        if form.is_valid():
            form.save()
            return redirect('lead_list')
    else:
        form = LeadForm(instance=lead)

    return render(request, 'lead_management/lead_form.html', {
        'form': form,
        'lead_form_title': lead_form_title,
    })


def delete_lead(request, lead_id):
    lead = get_object_or_404(RestaurantLead, id=lead_id)

    if request.method == 'POST':  # Confirm deletion
        lead.delete()
        return redirect('lead_list')  # Redirect to the list of leads

    return render(request, 'lead_management/delete_lead.html', {'lead': lead})
from django.shortcuts import render
from django.utils.timezone import now
from ..models import Call  # Ensure the model is correctly imported

def pending_calls_view(request):
    # Get today's date
    today = now().date()
    
    # Filter calls requiring follow-up and scheduled for today
    pending_calls = Call.objects.filter(
        follow_up_required=True,  # Follow-up is required
        scheduled_time__date=today,  # Scheduled for today
        status='pending' 
    ).order_by('scheduled_time')

    # Render the template with the filtered calls
    print(f"Date Filter: {today}")
    print(f"Pending Calls Count: {pending_calls.count()}")
    for call in pending_calls:
        print(f"Call ID: {call.id}, Lead: {call.lead}, Lead ID: {call.lead.id if call.lead else 'None'}")

    return render(request, 'lead_management/dashboard.html', {'pending_calls': pending_calls})

def mark_call_completed(request, purpose):
        
        # Attempt to retrieve the Call object using lead_id
        all_calls = Call.objects.all()
        print("all call count ", all_calls.count())
        for call in all_calls:
            print(f"Call ID: {call.id}, Lead: {call.lead.restaurant_name}, "
          f"Purpose: {call.purpose}, Follow-Up Required: {call.follow_up_required}")

        call = Call.objects.get(purpose=purpose)
        # print(Call.objects.all)
        # call.delete()
        # print(call)
        # Update the call object
        call.follow_up_required = False
        call.save()

        # Success message and redirect
        messages.success(request, "Call marked as completed successfully.")
        return redirect('dashboard')


def edit_call(request, call_id):
    CallForm = modelform_factory(Call, exclude=[])
    call = get_object_or_404(Call, id=call_id)

    if request.method == 'POST':
        form = CallForm(request.POST, instance=call)
        if form.is_valid():
            form.save()
            return redirect('dashboard')  # Redirect to the appropriate page after editing
    else:
        form = CallForm(instance=call)

    return render(request, 'lead_management/edit_call.html', {'form': form})