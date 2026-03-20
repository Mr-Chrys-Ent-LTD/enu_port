# MRCHRYS ENT NIG LTD Website

A professional, multi-industry company website for MRCHRYS ENT NIG LTD - a Nigerian company offering telecom, software, cybersecurity, engineering, logistics, and general contract services.

## 🌟 Features

- **Responsive Design**: Mobile-first approach with Bootstrap 5
- **Modern UI**: Clean, professional design with dark blue and orange color scheme
- **Multiple Pages**: Home, About, Services, Projects, Contact
- **Contact Form**: Fully functional contact form with Django backend
- **Service Showcase**: Comprehensive listing of 10+ service categories
- **Portfolio Section**: Project management and showcase
- **WhatsApp Integration**: Direct messaging capability
- **Admin Panel**: Django admin interface for managing content
- **SEO Friendly**: Proper meta tags and semantic HTML
- **Fast & Secure**: Built with Django security best practices

## 🛠️ Technology Stack

### Backend
- **Framework**: Django 4.2
- **Database**: SQLite (default, easily scalable to PostgreSQL)
- **Python**: 3.8+

### Frontend
- **HTML5** & **CSS3**
- **Bootstrap 5**: Responsive framework
- **FontAwesome 6**: Icon library
- **Vanilla JavaScript**: Modern interactions and animations

### Optional
- Django REST Framework (for API)
- Celery (for async tasks)

## 📋 Project Structure

```
enu/
├── manage.py
├── requirements.txt
├── README.md
├── db.sqlite3
├── mrchrys_project/           # Project configuration
│   ├── __init__.py
│   ├── settings.py           # Django settings
│   ├── urls.py              # URL routing
│   ├── wsgi.py              # WSGI application
│   └── asgi.py              # ASGI application
├── website/                   # Main app
│   ├── __init__.py
│   ├── admin.py             # Admin customization
│   ├── apps.py              # App configuration
│   ├── models.py            # Database models
│   ├── views.py             # View functions
│   ├── urls.py              # App URL patterns
│   ├── forms.py             # Django forms
│   ├── templatetags/        # Custom template tags
│   ├── templates/           # HTML templates
│   │   ├── base.html
│   │   └── website/
│   │       ├── home.html
│   │       ├── about.html
│   │       ├── services.html
│   │       ├── projects.html
│   │       └── contact.html
│   └── static/              # Static files
│       ├── css/
│       │   └── style.css
│       ├── js/
│       │   └── script.js
│       └── images/
└── media/                    # User-uploaded files
```

## 🚀 Getting Started

### Prerequisites
- Python 3.8 or higher
- pip (Python package manager)
- Virtual environment (recommended)

### Installation Steps

1. **Clone or Extract the Project**
   ```bash
   cd enu
   ```

2. **Create a Virtual Environment** (Recommended)
   ```bash
   # On Windows
   python -m venv venv
   venv\Scripts\activate

   # On macOS/Linux
   python3 -m venv venv
   source venv/bin/activate
   ```

3. **Install Dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Run Migrations**
   ```bash
   python manage.py migrate
   ```

5. **Create a Superuser** (For admin access)
   ```bash
   python manage.py createsuperuser
   ```
   Follow the prompts to create an admin account.

6. **Collect Static Files** (For production)
   ```bash
   python manage.py collectstatic --noinput
   ```

7. **Run the Development Server**
   ```bash
   python manage.py runserver
   ```

8. **Access the Website**
   - Main site: http://localhost:8000
   - Admin panel: http://localhost:8000/admin

## 📄 Configuration

### Settings File (`mrchrys_project/settings.py`)

Key configurations:

```python
# Database (Change to PostgreSQL for production)
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

# Static Files
STATIC_URL = '/static/'
STATIC_ROOT = BASE_DIR / 'staticfiles'

# Media Files  
MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR / 'media'

# Email Configuration
EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'
```

### Email Configuration

For production, update the email backend in `settings.py`:

```python
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'your-email-host'
EMAIL_PORT = 587
EMAIL_USE_TLS = True
EMAIL_HOST_USER = 'your-email@example.com'
EMAIL_HOST_PASSWORD = 'your-password'
DEFAULT_FROM_EMAIL = 'your-email@example.com'
```

### Update Company Information

Company information is stored in `website/views.py`. Update the `COMPANY_INFO` dictionary:

```python
COMPANY_INFO = {
    'name': 'MRCHRYS ENT NIG LTD',
    'email': 'info@mrchrys.com',
    'phone': '+234 (0) 123 456 7890',
    'whatsapp': '+2341234567890',
    'address': 'Lagos, Nigeria',
    # ... other fields
}
```

## 📦 Models

### ContactMessage
Stores contact form submissions with timestamps and read status.

```python
class ContactMessage(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=20, blank=True, null=True)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    is_read = models.BooleanField(default=False)
```

### Service
Manages service categories and descriptions for the services page.

```python
class Service(models.Model):
    category = models.CharField(max_length=100)
    title = models.CharField(max_length=200)
    description = models.TextField()
    icon = models.CharField(max_length=50)
    order = models.IntegerField(default=0)
```

### Project
Manages portfolio projects with images and categories.

```python
class Project(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    category = models.CharField(max_length=100)
    image = models.ImageField(upload_to='projects/')
    completion_date = models.DateField(blank=True, null=True)
    order = models.IntegerField(default=0)
```

## 🎨 Customization

### Color Scheme

The website uses a dark blue and orange color scheme. Modify colors in `website/static/css/style.css`:

```css
:root {
    --primary-color: #003d82;      /* Dark Blue */
    --secondary-color: #ff9500;    /* Orange */
    --dark-color: #1a1a1a;
    --light-color: #f8f9fa;
    --white-color: #ffffff;
}
```

### Logo & Branding

To add a logo, update the navbar brand in `website/templates/base.html`:

```html
<a class="navbar-brand" href="{% url 'home' %}">
    <img src="{% static 'images/logo.png' %}" alt="Logo" height="40">
    MRCHRYS ENT
</a>
```

### Service Icons

Service icons are defined using FontAwesome classes. Update in `website/views.py`:

```python
SERVICE_ICONS = {
    'Telecommunications': 'fas fa-tower-cell',
    'Software & IT': 'fas fa-code',
    # ... more services
}
```

## 🔒 Security

### Production Checklist

Before deploying to production:

1. Set `DEBUG = False` in settings.py
2. Change `SECRET_KEY` to a secure random value
3. Set `ALLOWED_HOSTS` to your domain
4. Configure database (PostgreSQL recommended)
5. Set up email backend for form submissions
6. Configure HTTPS/SSL
7. Set secure cookie settings
8. Enable CSRF protection
9. Run security checks: `python manage.py check --deploy`

### Security Recommendations

```python
# settings.py for production
DEBUG = False
ALLOWED_HOSTS = ['yourdomain.com', 'www.yourdomain.com']

# Security headers
SECURE_SSL_REDIRECT = True
SESSION_COOKIE_SECURE = True
CSRF_COOKIE_SECURE = True
SECURE_HSTS_SECONDS = 31536000
SECURE_HSTS_INCLUDE_SUBDOMAINS = True
```

## 📊 Admin Panel Usage

### Access Admin Panel
Navigate to `/admin` and log in with your superuser credentials.

### Managing Content

**Contact Messages:**
- View submitted contact forms
- Mark as read
- Export for follow-up

**Services:**
- Add/edit service categories
- Manage service descriptions
- Set display order

**Projects:**
- Upload project images
- Add project details
- Manage portfolio

## 🚀 Deployment

### Heroku Deployment

1. Install Heroku CLI
2. Create `Procfile`:
   ```
   web: gunicorn mrchrys_project.wsgi
   ```

3. Create `runtime.txt`:
   ```
   python-3.11.0
   ```

4. Update `requirements.txt`:
   ```bash
   pip freeze > requirements.txt
   ```

5. Deploy:
   ```bash
   heroku login
   heroku create your-app-name
   git push heroku main
   ```

### Docker Deployment

1. Create `Dockerfile`:
   ```dockerfile
   FROM python:3.11
   WORKDIR /app
   COPY requirements.txt .
   RUN pip install -r requirements.txt
   COPY . .
   CMD ["gunicorn", "mrchrys_project.wsgi"]
   ```

2. Build and run:
   ```bash
   docker build -t mrchrys .
   docker run -p 8000:8000 mrchrys
   ```

## 🐛 Troubleshooting

### Static Files Not Loading

```bash
python manage.py collectstatic
# In settings.py, ensure STATIC_ROOT and STATICFILES_DIRS are correct
```

### Database Errors

```bash
python manage.py migrate
python manage.py makemigrations website
python manage.py migrate
```

### Form Not Submitting

1. Check CSRF token is in form
2. Verify email configuration
3. Check browser console for JavaScript errors

### Images Not Displaying

1. Ensure Pillow is installed: `pip install Pillow`
2. Check MEDIA_URL and MEDIA_ROOT settings
3. Verify file paths in templates

## 📚 Additional Resources

- [Django Documentation](https://docs.djangoproject.com/)
- [Bootstrap 5 Documentation](https://getbootstrap.com/docs/5.0/)
- [FontAwesome Icons](https://fontawesome.com/icons)

## 📝 License

This project is provided as-is for MRCHRYS ENT NIG LTD.

## 👥 Support & Contact

For inquiries or support:
- **Email**: info@mrchrys.com
- **Phone**: +234 (0) 123 456 7890
- **WhatsApp**: +2341234567890

---

**Last Updated**: March 2024  
**Django Version**: 4.2+  
**Python Version**: 3.8+
