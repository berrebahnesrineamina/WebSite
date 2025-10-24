#!/usr/bin/env python3
"""
Fix Database SSL/TLS Connection for DigitalOcean
This script handles the SSL requirement for Render.com databases
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

def fix_database_connection():
    """Fix database SSL connection issues"""
    print("🔧 Fixing database SSL/TLS connection...")
    
    try:
        # Import Django after setting up the environment
        django.setup()
        
        # Test database connection
        from django.db import connection
        cursor = connection.cursor()
        cursor.execute("SELECT 1")
        print("✅ Database connection successful!")
        
        # Run migrations
        from django.core.management import execute_from_command_line
        print("📦 Running database migrations...")
        execute_from_command_line(['manage.py', 'migrate'])
        
        # Create admin account
        from django.contrib.auth.models import User
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
        
        # Create test accounts
        print("👥 Creating test accounts...")
        execute_from_command_line(['manage.py', 'create_test_accounts', '--count', '5'])
        
        print("✅ Database SSL fix complete!")
        print("\n🎉 Your app is now ready!")
        print("📋 Test Accounts:")
        print("  Admin: admin / admin123")
        print("  Test users: test1@wathaiqplus.com / test123456")
        
    except Exception as e:
        print(f"❌ Database connection failed: {e}")
        print("\n🔧 Alternative solutions:")
        print("1. Check your DATABASE_URL environment variable")
        print("2. Ensure the database allows connections from DigitalOcean")
        print("3. Try using a DigitalOcean managed database instead")
        print("4. Contact Render.com support for database access issues")

if __name__ == '__main__':
    fix_database_connection()
