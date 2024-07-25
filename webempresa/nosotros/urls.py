from django.urls import path
from . import views 


app_name = 'nosotros'

urlpatterns = [
    path('', views.NosotrosListView.as_view(), name= 'nosotros_list'),
    path('<int:pk>/', views.NosotrosDetailView.as_view(), name='nosotros_detail'),
]