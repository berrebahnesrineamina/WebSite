"""
Database configuration helper for DigitalOcean deployment
Handles SSL/TLS requirements for different database providers
"""
import os
import dj_database_url
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent

def get_database_config():
    """
    Get database configuration based on environment
    Handles SSL requirements for different providers
    """
    if os.getenv('DATABASE_URL'):
        # Production database (PostgreSQL)
        db_config = dj_database_url.parse(os.getenv('DATABASE_URL'))
        
        # Check if it's a Render.com database (requires SSL)
        if 'render.com' in db_config.get('HOST', ''):
            # Render.com requires SSL
            db_config['OPTIONS'] = {
                'sslmode': 'require',
            }
        elif 'digitalocean.com' in db_config.get('HOST', ''):
            # DigitalOcean managed database
            db_config['OPTIONS'] = {
                'sslmode': 'require',
            }
        else:
            # Other providers - try without SSL first
            db_config['OPTIONS'] = {
                'sslmode': 'prefer',
            }
        
        return {
            'default': db_config
        }
    else:
        # Development database (SQLite)
        return {
            'default': {
                'ENGINE': 'django.db.backends.sqlite3',
                'NAME': BASE_DIR / 'db.sqlite3',
            }
        }
