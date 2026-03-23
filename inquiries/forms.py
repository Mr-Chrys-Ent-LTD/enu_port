"""Forms for service inquiries and service projects."""
from django import forms
from .models import ServiceInquiry
from cybersecurity.models import SecurityProject
from telecommunications.models import TelecomProject
from software_dev.models import DevProject
from engineering.models import EngineeringProject
from logistics.models import LogisticsProject
from contracting.models import ContractingProject
from electrical_power.models import ElectricalProject
from entertainment_media.models import EntertainmentProject
from training_consulting.models import TrainingProject


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


# ==================== SERVICE PROJECT FORMS ====================

class SecurityProjectForm(forms.ModelForm):
    """Form for creating/editing cybersecurity projects."""
    class Meta:
        model = SecurityProject
        fields = ['title', 'description', 'client', 'featured_image',
                  'completion_date', 'result', 'order']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Project Title'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'rows': 5}),
            'client': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Client Name'}),
            'featured_image': forms.FileInput(attrs={'class': 'form-control'}),
            'completion_date': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'result': forms.Textarea(attrs={'class': 'form-control', 'rows': 4}),
            'order': forms.NumberInput(attrs={'class': 'form-control'}),
        }


class TelecomProjectForm(forms.ModelForm):
    """Form for creating/editing telecommunications projects."""
    class Meta:
        model = TelecomProject
        fields = ['title', 'description', 'client', 'featured_image',
                  'completion_date', 'result', 'order']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Project Title'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'rows': 5}),
            'client': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Client Name'}),
            'featured_image': forms.FileInput(attrs={'class': 'form-control'}),
            'completion_date': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'result': forms.Textarea(attrs={'class': 'form-control', 'rows': 4}),
            'order': forms.NumberInput(attrs={'class': 'form-control'}),
        }


class DevProjectForm(forms.ModelForm):
    """Form for creating/editing software development projects."""
    class Meta:
        model = DevProject
        fields = ['title', 'description', 'client', 'technologies', 'featured_image',
                  'completion_date', 'result', 'order']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Project Title'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'rows': 5}),
            'client': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Client Name'}),
            'technologies': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'e.g., Python, Django, PostgreSQL'}),
            'featured_image': forms.FileInput(attrs={'class': 'form-control'}),
            'completion_date': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'result': forms.Textarea(attrs={'class': 'form-control', 'rows': 4}),
            'order': forms.NumberInput(attrs={'class': 'form-control'}),
        }


class EngineeringProjectForm(forms.ModelForm):
    """Form for creating/editing engineering projects."""
    class Meta:
        model = EngineeringProject
        fields = ['title', 'description', 'client', 'featured_image',
                  'completion_date', 'result', 'order']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Project Title'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'rows': 5}),
            'client': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Client Name'}),
            'featured_image': forms.FileInput(attrs={'class': 'form-control'}),
            'completion_date': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'result': forms.Textarea(attrs={'class': 'form-control', 'rows': 4}),
            'order': forms.NumberInput(attrs={'class': 'form-control'}),
        }


class LogisticsProjectForm(forms.ModelForm):
    """Form for creating/editing logistics projects."""
    class Meta:
        model = LogisticsProject
        fields = ['title', 'description', 'client', 'featured_image',
                  'completion_date', 'result', 'order']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Project Title'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'rows': 5}),
            'client': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Client Name'}),
            'featured_image': forms.FileInput(attrs={'class': 'form-control'}),
            'completion_date': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'result': forms.Textarea(attrs={'class': 'form-control', 'rows': 4}),
            'order': forms.NumberInput(attrs={'class': 'form-control'}),
        }


class ContractingProjectForm(forms.ModelForm):
    """Form for creating/editing contracting projects."""
    class Meta:
        model = ContractingProject
        fields = ['title', 'description', 'client', 'featured_image',
                  'completion_date', 'result', 'order']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Project Title'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'rows': 5}),
            'client': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Client Name'}),
            'featured_image': forms.FileInput(attrs={'class': 'form-control'}),
            'completion_date': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'result': forms.Textarea(attrs={'class': 'form-control', 'rows': 4}),
            'order': forms.NumberInput(attrs={'class': 'form-control'}),
        }


class ElectricalProjectForm(forms.ModelForm):
    """Form for creating/editing electrical and power projects."""
    class Meta:
        model = ElectricalProject
        fields = ['title', 'description', 'client', 'featured_image',
                  'completion_date', 'result', 'order']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Project Title'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'rows': 5}),
            'client': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Client Name'}),
            'featured_image': forms.FileInput(attrs={'class': 'form-control'}),
            'completion_date': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'result': forms.Textarea(attrs={'class': 'form-control', 'rows': 4}),
            'order': forms.NumberInput(attrs={'class': 'form-control'}),
        }


class EntertainmentProjectForm(forms.ModelForm):
    """Form for creating/editing entertainment and media projects."""
    class Meta:
        model = EntertainmentProject
        fields = ['title', 'description', 'client', 'featured_image',
                  'completion_date', 'result', 'order']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Project Title'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'rows': 5}),
            'client': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Client Name'}),
            'featured_image': forms.FileInput(attrs={'class': 'form-control'}),
            'completion_date': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'result': forms.Textarea(attrs={'class': 'form-control', 'rows': 4}),
            'order': forms.NumberInput(attrs={'class': 'form-control'}),
        }


class TrainingProjectForm(forms.ModelForm):
    """Form for creating/editing training and consulting projects."""
    class Meta:
        model = TrainingProject
        fields = ['title', 'description', 'client', 'featured_image',
                  'completion_date', 'result', 'order']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Project Title'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'rows': 5}),
            'client': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Client Name'}),
            'featured_image': forms.FileInput(attrs={'class': 'form-control'}),
            'completion_date': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'result': forms.Textarea(attrs={'class': 'form-control', 'rows': 4}),
            'order': forms.NumberInput(attrs={'class': 'form-control'}),
        }
