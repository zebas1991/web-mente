from django.shortcuts import render
from .models import Service
from django.views.generic import ListView, DetailView
# Create your views here.

class ServicesListView(ListView):
    model = Service
    template_name = 'services/services_list.html'
    context_object_name = 'services'

    
   
class ServicesDetailView(DetailView):
    model= Service
    template_name = 'services/services_detail.html'
    context_object_name = 'service'


   
   
   
   
   
