#!/usr/bin/env python3
"""
DigitalOcean Deployment Script for Wathaiq Plus
This script helps set up test accounts and configure the app for DigitalOcean
"""

import os
import sys
import django
from pathlib import Path

# Add the project directory to Python path
BASE_DIR = Path(__file__).resolve().parent
sys.path.append(str(BASE_DIR))

# Set Django settings
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'project.settings')
django.setup()

from django.core.management import execute_from_command_line
from django.contrib.auth.models import User
from pages.models import Client
from django.contrib.auth.hashers import make_password

def setup_digitalocean():
    """Setup the application for DigitalOcean deployment"""
    print("🚀 Setting up Wathaiq Plus for DigitalOcean deployment...")
    
    # 1. Run migrations
    print("📦 Running database migrations...")
    execute_from_command_line(['manage.py', 'migrate'])
    
    # 2. Collect static files
    print("📁 Collecting static files...")
    execute_from_command_line(['manage.py', 'collectstatic', '--noinput'])
    
    # 3. Create superuser if doesn't exist
    print("👤 Creating admin superuser...")
    if not User.objects.filter(username='admin').exists():
        User.objects.create_superuser(
            username='admin',
            email='admin@wathaiqplus.com',
            password='admin123'
        )
        print("✅ Admin account created: admin / admin123")
    else:
        print("ℹ️  Admin account already exists")
    
    # 4. Create test accounts
    print("👥 Creating test accounts...")
    execute_from_command_line(['manage.py', 'create_test_accounts', '--count', '10'])
    
    print("✅ DigitalOcean setup complete!")
    print("\n📋 Test Accounts Created:")
    print("=" * 50)
    print("Admin Account:")
    print("  Username: admin")
    print("  Password: admin123")
    print("  URL: /admin/")
    print("\nTest Client Accounts:")
    print("  Email: test1@wathaiqplus.com")
    print("  Password: test123456")
    print("  Email: test2@wathaiqplus.com")
    print("  Password: test123456")
    print("  ... (and 8 more)")
    print("\n🔗 Access your app at your DigitalOcean domain!")

if __name__ == '__main__':
    setup_digitalocean()
