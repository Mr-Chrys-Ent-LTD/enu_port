"""URL patterns for inquiries app."""
from django.urls import path
from . import views
from . import admin_views

app_name = 'inquiries'

urlpatterns = [
    # Inquiry submission endpoints
    path('submit/', views.submit_inquiry, name='submit'),
    path('submit/<str:service>/', views.submit_inquiry, name='submit_service'),
    path('list/', views.inquiry_list, name='list'),
    path('<int:pk>/', views.inquiry_detail, name='detail'),

    # Admin dashboard endpoints
    path('admin/dashboard/', admin_views.admin_dashboard, name='admin_dashboard'),

    # Create endpoints
    path('admin/create-inquiry/', admin_views.create_inquiry, name='create_inquiry'),
    path('admin/create-message/', admin_views.create_contact_message,
         name='create_contact_message'),

    # Detail & manage endpoints
    path('admin/inquiry/<int:inquiry_id>/',
         admin_views.inquiry_detail, name='inquiry_detail'),
    path('admin/inquiry/<int:inquiry_id>/edit/',
         admin_views.edit_inquiry, name='edit_inquiry'),
    path('admin/inquiry/<int:inquiry_id>/mark-read/',
         admin_views.mark_as_read, name='mark_as_read'),
    path('admin/inquiry/<int:inquiry_id>/delete/',
         admin_views.delete_inquiry, name='delete_inquiry'),

    path('admin/message/<int:message_id>/',
         admin_views.contact_message_detail, name='contact_message_detail'),
    path('admin/message/<int:message_id>/edit/',
         admin_views.edit_contact_message, name='edit_contact_message'),
    path('admin/message/<int:message_id>/delete/',
         admin_views.delete_contact_message, name='delete_contact_message'),

    # Project management
    path('admin/projects/', admin_views.projects_list, name='projects_list'),
    path('admin/create-project/', admin_views.create_project, name='create_project'),
    path('admin/project/<int:project_id>/',
         admin_views.project_detail, name='project_detail'),
    path('admin/project/<int:project_id>/edit/',
         admin_views.edit_project, name='edit_project'),
    path('admin/project/<int:project_id>/delete/',
         admin_views.delete_project, name='delete_project'),
]
