from my_portfolio.settings import *
import os

# Override settings for production environment

# SECURITY WARNING: Set DEBUG to False in production!
DEBUG = False

# Secret key for production (should be set in the environment variables)
SECRET_KEY = os.getenv('SECRET_KEY')

# Allow only specific domains in production (you should restrict this)
ALLOWED_HOSTS = ['*']  # Replace with your actual production domain

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',  # For serving static files in development and production
    'django.contrib.sessions.middleware.SessionMiddleware',
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

# Database settings for production (use environment variables)
import dj_database_url

DATABASES = {
    'default': dj_database_url.config(default=os.getenv('DATABASE_URL'))
}

# Email settings for production (using environment variables for Gmail SMTP)
EMAIL_HOST_USER = os.getenv('EMAIL_HOST_USER')
EMAIL_HOST_PASSWORD = os.getenv('EMAIL_HOST_PASSWORD')
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587
EMAIL_USE_TLS = True

# CORS settings for production (restrict origins to your frontend)
CORS_ALLOWED_ORIGINS = [
    "https://mangalbodele.netlify.app",  # Replace with your production frontend domain
]

# Static files settings for production (WhiteNoise will serve static files)
STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')

# Enable WhiteNoise to serve static files in production

# Security settings for production
SECURE_SSL_REDIRECT = True  # Redirect HTTP to HTTPS
CSRF_COOKIE_SECURE = True  # Ensure CSRF cookie is only sent over HTTPS
SESSION_COOKIE_SECURE = True  # Ensure session cookie is only sent over HTTPS
SECURE_BROWSER_XSS_FILTER = True
SECURE_CONTENT_TYPE_NOSNIFF = True
X_FRAME_OPTIONS = 'DENY'

# Additional configurations for production (e.g., logging, caching, etc.) can be added here
