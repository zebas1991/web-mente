from django.shortcuts import render
from .models import Nosotros
from django.views.generic import ListView, DetailView
# Create your views here.

class NosotrosListView(ListView):
    model = Nosotros
    template_name = 'nosotros/nosotros_list.html'
    context_object_name = 'nosotros_list'

class NosotrosDetailView(DetailView):
    model = Nosotros
    template_name = 'nosotros/nosotros_detail.html'
    context_object_name = 'tu'



