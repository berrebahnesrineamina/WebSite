"""
Database configuration for DigitalOcean deployment
Configured to use DigitalOcean managed database instead of Render.com
"""
import os
import dj_database_url
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent

def get_database_config():
    """
    Get database configuration for DigitalOcean deployment
    Uses DigitalOcean managed database instead of Render.com
    """
    # Check for DigitalOcean database URL first
    digitalocean_db_url = os.getenv('DIGITALOCEAN_DATABASE_URL')
    render_db_url = os.getenv('DATABASE_URL')
    
    if digitalocean_db_url:
        # Use DigitalOcean managed database (preferred)
        print("Using DigitalOcean managed database")
        db_config = dj_database_url.parse(digitalocean_db_url)
        db_config['OPTIONS'] = {
            'sslmode': 'require',
        }
        return {
            'default': db_config
        }
    elif render_db_url and 'render.com' not in render_db_url:
        # Use other database if not Render.com
        print("Using alternative database (not Render.com)")
        db_config = dj_database_url.parse(render_db_url)
        db_config['OPTIONS'] = {
            'sslmode': 'prefer',
        }
        return {
            'default': db_config
        }
    else:
        # Development database (SQLite) or fallback
        print("Using SQLite database (development/fallback)")
        return {
            'default': {
                'ENGINE': 'django.db.backends.sqlite3',
                'NAME': BASE_DIR / 'db.sqlite3',
            }
        }
