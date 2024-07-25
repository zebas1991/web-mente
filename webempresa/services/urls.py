# services/urls.py

from django.urls import path
from . import views

app_name = 'services'

urlpatterns = [
    path('', views.ServicesListView.as_view(), name='services_list'),
    path('<int:pk>/', views.ServicesDetailView.as_view(), name='services_detail'),
]
