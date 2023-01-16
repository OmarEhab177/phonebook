from django.urls import path
from . import views

urlpatterns = [
    path('', views.contact_list, name='contact-list'),
    path('create-contact/', views.create_contact_with_numbers, name='contact-create'),
    path('contacts/<int:pk>/', views.contact_detail, name='contact_detail'),
]
