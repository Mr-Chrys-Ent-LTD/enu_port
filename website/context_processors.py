"""
Context processors for website app.
These functions are called for every template render to inject global context.
"""


def service_apps_context(request):
    """
    Inject service_apps into all template contexts.
    This allows all templates that inherit from base.html to access service navigation.
    """
    service_apps = {
        'Telecommunications': {
            'name': 'Telecommunications',
            'url': '/telecommunications/',
            'icon': 'fas fa-tower-cell',
            'description': 'Network design, installation, and maintenance services'
        },
        'Software & IT': {
            'name': 'Software Development',
            'url': '/software-dev/',
            'icon': 'fas fa-code',
            'description': 'Custom software solutions and development services'
        },
        'Cybersecurity': {
            'name': 'Cybersecurity',
            'url': '/cybersecurity/',
            'icon': 'fas fa-shield-alt',
            'description': 'Security audits, testing, and threat monitoring'
        },
        'Engineering & Construction': {
            'name': 'Engineering',
            'url': '/engineering/',
            'icon': 'fas fa-hard-hat',
            'description': 'Engineering consulting and implementation services'
        },
        'Logistics & Supply': {
            'name': 'Logistics',
            'url': '/logistics/',
            'icon': 'fas fa-truck',
            'description': 'Supply chain and logistics management'
        },
        'General Contracts': {
            'name': 'General Contracting',
            'url': '/contracting/',
            'icon': 'fas fa-handshake',
            'description': 'Professional contracting and project management'
        },
    }

    return {
        'service_apps': service_apps,
    }
