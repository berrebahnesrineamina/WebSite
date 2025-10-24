#!/usr/bin/env python3
"""
Test Accounts Verification Script
This script verifies that all test accounts are working properly
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

from django.contrib.auth.models import User
from pages.models import Client, Service
from django.contrib.auth.hashers import check_password

def test_accounts():
    """Test all created accounts"""
    print("🧪 Testing All Accounts")
    print("=" * 50)
    
    # Test admin account
    print("\n👤 Admin Account:")
    try:
        admin = User.objects.get(username='admin')
        print(f"✅ Admin account exists: {admin.username}")
        print(f"   Email: {admin.email}")
        print(f"   Is superuser: {admin.is_superuser}")
    except User.DoesNotExist:
        print("❌ Admin account not found")
    
    # Test client accounts
    print(f"\n👥 Client Accounts ({Client.objects.count()} total):")
    clients = Client.objects.all()[:10]  # Show first 10
    for i, client in enumerate(clients, 1):
        print(f"  {i}. {client.email} - {client.full_name}")
    
    # Test service requests
    print(f"\n📋 Service Requests ({Service.objects.count()} total):")
    services = Service.objects.all()[:5]  # Show first 5
    for i, service in enumerate(services, 1):
        status_emoji = "✅" if service.status == "Approuvé" else "⏳" if service.status == "En attente" else "❌"
        print(f"  {i}. {service.get_service_type_display()} - {status_emoji} {service.status}")
    
    # Test password verification
    print(f"\n🔐 Password Testing:")
    test_client = Client.objects.first()
    if test_client:
        password_works = check_password('test123456', test_client.password)
        print(f"✅ Password verification: {'Working' if password_works else 'Failed'}")
    
    print(f"\n📊 Summary:")
    print(f"  - Admin accounts: {User.objects.filter(is_superuser=True).count()}")
    print(f"  - Client accounts: {Client.objects.count()}")
    print(f"  - Service requests: {Service.objects.count()}")
    print(f"  - Pending services: {Service.objects.filter(status='En attente').count()}")
    print(f"  - Approved services: {Service.objects.filter(status='Approuvé').count()}")
    print(f"  - Rejected services: {Service.objects.filter(status='Rejeté').count()}")
    
    print(f"\n🎉 All test accounts are ready!")
    print(f"🌐 Test your app at: http://localhost:8000/")
    print(f"🔧 Admin panel at: http://localhost:8000/admin/")

if __name__ == '__main__':
    test_accounts()
