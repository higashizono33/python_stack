from django.shortcuts import render
from .models import Lead
from django.core.paginator import Paginator
from django.views.generic import ListView
from datetime import datetime

class LeadList(ListView):
    template_name = 'index.html'
    paginate_by = 20
    model = Lead

def filter_from_date(request):
    start_date = datetime.strptime(request.POST['from_date'], '%m/%d/%Y')
    end_date = datetime.now()
    page_obj = Lead.objects.filter(registered_at__range=(start_date, end_date))
    
    return render(request, 'index.html', {'page_obj': page_obj})


def filter_date(request):
    date = datetime.strptime(request.POST['date'], '%m/%d/%Y')
    page_obj = Lead.objects.filter(registered_at=date)
    # paginator = Paginator(leads, 20)
    # page_number = request.GET.get('page')
    # page_obj = paginator.get_page(page_number)

    return render(request, 'index.html', {'page_obj': page_obj})

def filter_name(request):
    page_obj = Lead.objects.filter(first_name__startswith=request.POST['name'])

    return render(request, 'index.html', {'page_obj': page_obj})
