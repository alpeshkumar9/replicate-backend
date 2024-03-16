from .base import *

# Production-specific settings
DEBUG = False
ALLOWED_HOSTS = ['yourdomain.com']

# Security settings for production
SECURE_SSL_REDIRECT = True
SESSION_COOKIE_SECURE = True
CSRF_COOKIE_SECURE = True
