/**
 * MRCHRYS ENT NIG LTD - Main JavaScript File
 * Custom functionality and interactions
 */

document.addEventListener('DOMContentLoaded', function () {
    // Initialize all features
    initializeNavbar();
    initializeAnimations();
    initializeFormValidation();
    initializeScrollEffects();
});

/**
 * Navbar Functionality
 */
function initializeNavbar() {
    const navbar = document.querySelector('.navbar');
    const navbarCollapse = document.querySelector('.navbar-collapse');
    const dropdownItem = document.querySelector('.nav-item.dropdown');

    // Handle hover for desktop (show dropdown on hover)
    if (dropdownItem) {
        dropdownItem.addEventListener('mouseenter', function () {
            if (window.innerWidth >= 992) {
                const dropdownToggle = this.querySelector('.nav-link.dropdown-toggle');
                const dropdownMenu = this.querySelector('.dropdown-menu');

                if (dropdownToggle && dropdownMenu) {
                    dropdownToggle.classList.add('show');
                    dropdownMenu.classList.add('show');
                    dropdownToggle.setAttribute('aria-expanded', 'true');
                }
            }
        });

        dropdownItem.addEventListener('mouseleave', function () {
            if (window.innerWidth >= 992) {
                const dropdownToggle = this.querySelector('.nav-link.dropdown-toggle');
                const dropdownMenu = this.querySelector('.dropdown-menu');

                if (dropdownToggle && dropdownMenu) {
                    dropdownToggle.classList.remove('show');
                    dropdownMenu.classList.remove('show');
                    dropdownToggle.setAttribute('aria-expanded', 'false');
                }
            }
        });
    }

    // Handle dropdown toggle to expand navbar if collapsed on mobile
    const dropdownToggle = document.querySelector('.nav-link.dropdown-toggle');
    if (dropdownToggle) {
        dropdownToggle.addEventListener('click', function (e) {
            // Check if navbar is collapsed (only on mobile < 992px)
            if (window.innerWidth < 992) {
                const bsCollapse = new bootstrap.Collapse(navbarCollapse, {
                    toggle: false
                });
                // If collapsed, show it
                if (!navbarCollapse.classList.contains('show')) {
                    bsCollapse.show();
                }
            }
        });
    }

    // Close mobile menu when regular nav link is clicked (but not dropdown items)
    const navLinks = document.querySelectorAll('.nav-link:not(.dropdown-toggle)');

    navLinks.forEach(link => {
        link.addEventListener('click', function () {
            const bsCollapse = new bootstrap.Collapse(navbarCollapse, {
                toggle: false
            });
            bsCollapse.hide();
        });
    });

    // Handle dropdown item clicks to close navbar
    const dropdownItems = document.querySelectorAll('.dropdown-item');
    dropdownItems.forEach(item => {
        item.addEventListener('click', function () {
            const bsCollapse = new bootstrap.Collapse(navbarCollapse, {
                toggle: false
            });
            bsCollapse.hide();
        });
    });

    // Add background on scroll
    window.addEventListener('scroll', function () {
        if (window.scrollY > 50) {
            navbar.style.boxShadow = '0 4px 12px rgba(0, 0, 0, 0.15)';
        } else {
            navbar.style.boxShadow = '0 2px 4px rgba(0, 0, 0, 0.1)';
        }
    });
}

/**
 * Scroll Animations
 */
function initializeAnimations() {
    // Observe elements for animation on scroll
    const observerOptions = {
        threshold: 0.1,
        rootMargin: '0px 0px -100px 0px'
    };

    const observer = new IntersectionObserver(function (entries) {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                entry.target.style.opacity = '1';
                entry.target.style.transform = 'translateY(0)';
            }
        });
    }, observerOptions);

    // Observe all cards and sections
    const animateElements = document.querySelectorAll('.card, .service-card, section');
    animateElements.forEach(el => {
        el.style.opacity = '0';
        el.style.transform = 'translateY(20px)';
        el.style.transition = 'all 0.6s ease-out';
        observer.observe(el);
    });
}

/**
 * Form Validation
 */
function initializeFormValidation() {
    const forms = document.querySelectorAll('form[novalidate]');

    forms.forEach(form => {
        form.addEventListener('submit', function (e) {
            if (!form.checkValidity()) {
                e.preventDefault();
                e.stopPropagation();
            }
            form.classList.add('was-validated');
        }, false);
    });
}

/**
 * Smooth Scroll Effects
 */
function initializeScrollEffects() {
    // Smooth scroll for anchor links
    document.querySelectorAll('a[href^="#"]').forEach(anchor => {
        anchor.addEventListener('click', function (e) {
            const href = this.getAttribute('href');
            if (href !== '#' && document.querySelector(href)) {
                e.preventDefault();
                Smooth.smoothScroolToTarget(href);
            }
        });
    });
}

/**
 * Utility Functions
 */

// Copy to clipboard function
function copyToClipboard(text) {
    navigator.clipboard.writeText(text).then(function () {
        showNotification('Copied to clipboard!', 'success');
    });
}

// Show notification function
function showNotification(message, type = 'info') {
    const alertHTML = `
        <div class="alert alert-${type} alert-dismissible fade show" role="alert" style="position: fixed; top: 20px; right: 20px; z-index: 9999;">
            ${message}
            <button type="button" class="btn-close" data-bs-dismiss="alert"></button>
        </div>
    `;

    document.body.insertAdjacentHTML('beforeend', alertHTML);

    // Auto-dismiss after 5 seconds
    setTimeout(() => {
        const alert = document.querySelector('.alert');
        if (alert) {
            const bsAlert = new bootstrap.Alert(alert);
            bsAlert.close();
        }
    }, 5000);
}

/**
 * Counter Animation (for statistics/achievements)
 */
function animateCounter(element, target, duration = 2000) {
    const start = 0;
    const increment = target / (duration / 16);
    let current = start;

    const counter = setInterval(() => {
        current += increment;
        if (current >= target) {
            element.textContent = target;
            clearInterval(counter);
        } else {
            element.textContent = Math.floor(current);
        }
    }, 16);
}

/**
 * Lazy Load Images
 */
function initializeLazyLoad() {
    if ('IntersectionObserver' in window) {
        const imageElements = document.querySelectorAll('img[loading="lazy"]');

        const imageObserver = new IntersectionObserver((entries, observer) => {
            entries.forEach(entry => {
                if (entry.isIntersecting) {
                    const img = entry.target;
                    img.src = img.dataset.src;
                    img.classList.add('loaded');
                    imageObserver.unobserve(img);
                }
            });
        });

        imageElements.forEach(img => imageObserver.observe(img));
    }
}

/**
 * Smooth Scroll Object
 */
const Smooth = {
    smoothScroolToTarget: function (target) {
        const element = document.querySelector(target);
        if (element) {
            const offsetTop = element.offsetTop - 100;
            window.scrollTo({
                top: offsetTop,
                behavior: 'smooth'
            });
        }
    }
};

/**
 * Initialize smooth scroll on page load
 */
window.addEventListener('load', function () {
    initializeLazyLoad();
});

/**
 * Handle messages/alerts dismissal
 */
document.addEventListener('DOMContentLoaded', function () {
    const alerts = document.querySelectorAll('.alert');
    alerts.forEach(alert => {
        // Auto-dismiss success alerts after 5 seconds
        if (alert.classList.contains('alert-success')) {
            setTimeout(() => {
                const bsAlert = new bootstrap.Alert(alert);
                bsAlert.close();
            }, 5000);
        }
    });
});

/**
 * Add active state to navbar based on current page
 */
function setActiveNavLink() {
    const currentLocation = location.pathname;
    const navLinks = document.querySelectorAll('.nav-link');

    navLinks.forEach(link => {
        const href = link.getAttribute('href');
        if (href === currentLocation || (currentLocation === '/' && href === '/')) {
            link.classList.add('active');
        } else {
            link.classList.remove('active');
        }
    });
}

document.addEventListener('DOMContentLoaded', setActiveNavLink);

/**
 * Service filter (if needed for multiple service pages)
 */
function filterServices(category) {
    const services = document.querySelectorAll('.service-card');

    services.forEach(service => {
        if (category === 'all' || service.dataset.category === category) {
            service.style.display = 'block';
            setTimeout(() => {
                service.style.opacity = '1';
            }, 10);
        } else {
            service.style.opacity = '0';
            setTimeout(() => {
                service.style.display = 'none';
            }, 300);
        }
    });
}

/**
 * Phone number formatting (optional)
 */
function formatPhoneNumber(phone) {
    const cleaned = ('' + phone).replace(/\D/g, '');
    const match = cleaned.match(/^(\d{3})(\d{3})(\d{4})$/);
    if (match) {
        return '(' + match[1] + ') ' + match[2] + '-' + match[3];
    }
    return phone;
}

/**
 * Handle WhatsApp contact button
 */
function initializeWhatsAppContact() {
    const whatsappButtons = document.querySelectorAll('[href*="wa.me"]');

    whatsappButtons.forEach(button => {
        button.addEventListener('click', function (e) {
            const isMobile = /Android|webOS|iPhone|iPad|iPod|BlackBerry|IEMobile|Opera Mini/i.test(navigator.userAgent);
            if (!isMobile && !button.target === '_blank') {
                e.preventDefault();
                showNotification('WhatsApp will open in a new window', 'info');
            }
        });
    });
}

document.addEventListener('DOMContentLoaded', initializeWhatsAppContact);

/**
 * Add scroll-to-top button
 */
function createScrollToTopButton() {
    const scrollBtn = document.createElement('button');
    scrollBtn.id = 'scrollToTop';
    scrollBtn.className = 'btn btn-primary p-3';
    scrollBtn.style.cssText = `
        position: fixed;
        bottom: 30px;
        right: 30px;
        display: none;
        z-index: 999;
        border-radius: 50%;
        width: 50px;
        height: 50px;
        padding: 0 !important;
        align-items: center;
        justify-content: center;
        box-shadow: 0 4px 12px rgba(0, 0, 0, 0.15);
    `;
    scrollBtn.innerHTML = '<i class="fas fa-arrow-up"></i>';
    scrollBtn.title = 'Go to top';

    document.body.appendChild(scrollBtn);

    window.addEventListener('scroll', function () {
        if (window.pageYOffset > 300) {
            scrollBtn.style.display = 'flex';
        } else {
            scrollBtn.style.display = 'none';
        }
    });

    scrollBtn.addEventListener('click', function () {
        window.scrollTo({
            top: 0,
            behavior: 'smooth'
        });
    });
}

document.addEventListener('DOMContentLoaded', createScrollToTopButton);

// Export functions if using modules
if (typeof module !== 'undefined' && module.exports) {
    module.exports = {
        copyToClipboard,
        showNotification,
        animateCounter,
        filterServices,
        formatPhoneNumber
    };
}
