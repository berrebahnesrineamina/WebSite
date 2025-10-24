#!/usr/bin/env python3
"""
Simple Test Accounts Verification
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

def test_accounts():
    """Test all created accounts"""
    print("Testing All Accounts")
    print("=" * 50)
    
    # Test admin account
    print("\nAdmin Account:")
    try:
        admin = User.objects.get(username='admin')
        print(f"SUCCESS: Admin account exists: {admin.username}")
        print(f"   Email: {admin.email}")
        print(f"   Is superuser: {admin.is_superuser}")
    except User.DoesNotExist:
        print("ERROR: Admin account not found")
    
    # Test client accounts
    client_count = Client.objects.count()
    print(f"\nClient Accounts ({client_count} total):")
    clients = Client.objects.all()[:10]  # Show first 10
    for i, client in enumerate(clients, 1):
        print(f"  {i}. {client.email} - {client.full_name}")
    
    # Test service requests
    service_count = Service.objects.count()
    print(f"\nService Requests ({service_count} total):")
    services = Service.objects.all()[:5]  # Show first 5
    for i, service in enumerate(services, 1):
        status_text = "APPROVED" if service.status == "Approuvé" else "PENDING" if service.status == "En attente" else "REJECTED"
        print(f"  {i}. {service.get_service_type_display()} - {status_text}")
    
    print(f"\nSummary:")
    print(f"  - Admin accounts: {User.objects.filter(is_superuser=True).count()}")
    print(f"  - Client accounts: {Client.objects.count()}")
    print(f"  - Service requests: {Service.objects.count()}")
    print(f"  - Pending services: {Service.objects.filter(status='En attente').count()}")
    print(f"  - Approved services: {Service.objects.filter(status='Approuvé').count()}")
    print(f"  - Rejected services: {Service.objects.filter(status='Rejeté').count()}")
    
    print(f"\nAll test accounts are ready!")
    print(f"Test your app at: http://localhost:8000/")
    print(f"Admin panel at: http://localhost:8000/admin/")

if __name__ == '__main__':
    test_accounts()
