"""Forms for service inquiries."""
from django import forms
from .models import ServiceInquiry


class ServiceInquiryForm(forms.ModelForm):
    """Form for submitting service inquiries."""

    class Meta:
        model = ServiceInquiry
        fields = ['name', 'email', 'phone', 'company',
                  'subject', 'message', 'budget', 'timeline']
        widgets = {
            'name': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Your Name',
                'required': True
            }),
            'email': forms.EmailInput(attrs={
                'class': 'form-control',
                'placeholder': 'your.email@example.com',
                'required': True
            }),
            'phone': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': '+234 XXX XXX XXXX',
            }),
            'company': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Your Company (Optional)',
            }),
            'subject': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Inquiry Subject',
                'required': True
            }),
            'message': forms.Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Tell us about your project or inquiry...',
                'rows': 6,
                'required': True
            }),
            'budget': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'e.g., $5,000 - $10,000',
            }),
            'timeline': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'e.g., 3 months',
            }),
        }
