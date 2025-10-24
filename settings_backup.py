# Backup settings for database connection issues
# Use this if the main settings.py doesn't work

# Simple database configuration that should work with most providers
import dj_database_url

if os.getenv('DATABASE_URL'):
    # Try with minimal SSL configuration
    DATABASES = {
        'default': dj_database_url.config(
            conn_max_age=600,
            ssl_require=False,  # Try without SSL first
        )
    }
else:
    # Development database (SQLite)
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': BASE_DIR / 'db.sqlite3',
        }
    }
