#!/usr/bin/env python3
"""
DigitalOcean Database Fix Script
This script fixes the database connection issues for DigitalOcean deployment
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

def fix_digitalocean_database():
    """Fix database connection and setup for DigitalOcean"""
    print("🔧 Fixing DigitalOcean database connection...")
    
    try:
        # 1. Test database connection
        print("📊 Testing database connection...")
        from django.db import connection
        cursor = connection.cursor()
        cursor.execute("SELECT 1")
        print("✅ Database connection successful!")
        
        # 2. Run migrations
        print("📦 Running database migrations...")
        execute_from_command_line(['manage.py', 'migrate'])
        
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
        execute_from_command_line(['manage.py', 'create_test_accounts', '--count', '5'])
        
        print("✅ DigitalOcean database fix complete!")
        print("\n📋 Test Accounts Available:")
        print("=" * 50)
        print("Admin Account:")
        print("  Username: admin")
        print("  Password: admin123")
        print("  URL: /admin/")
        print("\nTest Client Accounts:")
        clients = Client.objects.all()[:5]
        for client in clients:
            print(f"  Email: {client.email}")
            print(f"  Password: test123456")
        
    except Exception as e:
        print(f"❌ Database connection failed: {e}")
        print("\n🔧 Alternative solution:")
        print("1. Check your DATABASE_URL environment variable")
        print("2. Ensure the database is accessible from DigitalOcean")
        print("3. Consider using a DigitalOcean managed database")

if __name__ == '__main__':
    fix_digitalocean_database()
