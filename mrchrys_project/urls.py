"""
URL configuration for mrchrys_project.

This project supports both:
1. Monolithic structure: All services under main domain with different URL paths
2. Subdomain structure: Each service can be served as a separate app/subdomain

URL Patterns:
- Main website: / (home, about, services, contact)
- Telecommunications: /telecommunications/
- Software Development: /software-dev/
- Cybersecurity: /cybersecurity/
- Engineering: /engineering/
- Logistics: /logistics/
- General Contracting: /contracting/
- Electrical & Power: /electrical-power/
- Entertainment & Media: /entertainment-media/
- Training & Consulting: /training-consulting/
- Service Inquiries: /inquiries/ (shared across all services)
"""
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    # Admin interface
    path('admin/', admin.site.urls),

    # Main website (namespaced)
    path('', include(('website.urls', 'website'), namespace='website')),

    # Service-specific apps
    path('telecommunications/', include('telecommunications.urls')),
    path('software-dev/', include('software_dev.urls')),
    path('cybersecurity/', include('cybersecurity.urls')),
    path('engineering/', include('engineering.urls')),
    path('logistics/', include('logistics.urls')),
    path('contracting/', include('contracting.urls')),
    path('electrical-power/', include('electrical_power.urls')),
    path('entertainment-media/', include('entertainment_media.urls')),
    path('training-consulting/', include('training_consulting.urls')),

    # Shared inquiries app
    path('inquiries/', include('inquiries.urls')),
]

# Serve media files during development
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL,
                          document_root=settings.STATIC_ROOT)
