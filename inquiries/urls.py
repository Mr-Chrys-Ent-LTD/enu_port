"""URL patterns for inquiries app."""
from django.urls import path
from . import views

app_name = 'inquiries'

urlpatterns = [
    path('submit/', views.submit_inquiry, name='submit'),
    path('submit/<str:service>/', views.submit_inquiry, name='submit_service'),
    path('list/', views.inquiry_list, name='list'),
    path('<int:pk>/', views.inquiry_detail, name='detail'),
]
