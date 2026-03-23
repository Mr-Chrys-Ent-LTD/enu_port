"""
Forms for MRCHRYS ENT NIG LTD website.
"""
from django import forms
from .models import ContactMessage, Project, Service


class ContactForm(forms.ModelForm):
    """Form for contact message submissions."""

    class Meta:
        model = ContactMessage
        fields = ['name', 'email', 'phone', 'message']
        widgets = {
            'name': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Your Full Name',
                'required': True,
            }),
            'email': forms.EmailInput(attrs={
                'class': 'form-control',
                'placeholder': 'Your Email Address',
                'required': True,
            }),
            'phone': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Your Phone Number (Optional)',
            }),
            'message': forms.Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Your Message',
                'rows': 6,
                'required': True,
            }),
        }


class ProjectForm(forms.ModelForm):
    """Form for creating and editing projects."""

    category = forms.ChoiceField(
        required=True,
        widget=forms.Select(attrs={
            'class': 'form-select',
        }),
        help_text='Select the service category for this project'
    )

    class Meta:
        model = Project
        fields = ['title', 'description', 'category', 'client', 'image',
                  'completion_date', 'result', 'technologies', 'order']
        widgets = {
            'title': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Project Title',
                'required': True,
            }),
            'description': forms.Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Project Description',
                'rows': 5,
                'required': True,
            }),
            'client': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Client Name (Optional)',
            }),
            'image': forms.FileInput(attrs={
                'class': 'form-control',
                'accept': 'image/*',
            }),
            'completion_date': forms.DateInput(attrs={
                'class': 'form-control',
                'type': 'date',
            }),
            'result': forms.Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Project Outcome or Result',
                'rows': 4,
            }),
            'technologies': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Comma-separated technologies (e.g., Python, Django, PostgreSQL)',
            }),
            'order': forms.NumberInput(attrs={
                'class': 'form-control',
                'placeholder': 'Display order (0-100)',
            }),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Get unique categories from Service model
        categories = Service.objects.values_list(
            'category', flat=True).distinct().order_by('category')

        # Create choices list: (value, display_text)
        choices = [('', '-- Select a service category --')] + \
            [(cat, cat) for cat in categories]
        self.fields['category'].choices = choices
