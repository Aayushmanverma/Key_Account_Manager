from django.shortcuts import render, redirect
from django.db.models import Q
from django.utils.timezone import now
from datetime import date
from ..models import RestaurantLead, Interaction, Call
from django.forms import modelform_factory

def dashboard(request):
    # List all leads
    leads = RestaurantLead.objects.all()

    # Filter interactions requiring follow-up today
    today = date.today()
    pending_interactions = Interaction.objects.filter(
        follow_up_required=True, date=today
    )

    # Filter calls scheduled for today that are still pending
    today_time = now().date()
    pending_calls = Call.objects.filter(
        follow_up_required=True,
    )

    # Fetch recent interactions (last 10 interactions)
    recent_interactions = Interaction.objects.order_by('-date')[:10]

    # Basic search functionality for leads
    search_query = request.GET.get('q', '')
    if search_query:
        leads = leads.filter(
            Q(restaurant_name__icontains=search_query) |
            Q(address__icontains=search_query) |
            Q(assigned_kam__icontains=search_query)
        )

    # Handle adding a new lead
    LeadForm = modelform_factory(RestaurantLead, fields=('restaurant_name', 'address', 'contact_number', 'status', 'assigned_kam'))
    if request.method == 'POST':
        form = LeadForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('dashboard')  # Refresh the dashboard after saving
    else:
        form = LeadForm()

    context = {
        'leads': leads,
        'pending_interactions': pending_interactions,
        'pending_calls': pending_calls,
        'recent_interactions': recent_interactions,
        'search_query': search_query,
        'form': form,  # Include the form in the context
    }
    return render(request, 'lead_management/dashboard.html', context)
