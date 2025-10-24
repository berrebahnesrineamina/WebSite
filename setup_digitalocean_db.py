#!/usr/bin/env python3
"""
DigitalOcean Database Setup Helper
This script helps you configure the database connection
"""
import os

def show_database_setup_instructions():
    """Display step-by-step instructions for setting up DigitalOcean database"""
    
    print("🗄️  DigitalOcean Database Setup Guide")
    print("=" * 50)
    
    print("\n📋 Step 1: Create DigitalOcean Managed Database")
    print("1. Go to: https://cloud.digitalocean.com/databases")
    print("2. Click 'Create Database'")
    print("3. Choose: PostgreSQL, Basic plan ($15/month)")
    print("4. Select same region as your app")
    print("5. Name it: 'wathaiqplus-db'")
    
    print("\n📋 Step 2: Get Connection Details")
    print("After creation, you'll get:")
    print("- Host: db-postgresql-xxx-xxx.db.ondigitalocean.com")
    print("- Port: 25060 (usually)")
    print("- Database: defaultdb")
    print("- Username: doadmin")
    print("- Password: [your-password]")
    
    print("\n📋 Step 3: Update Environment Variables")
    print("In DigitalOcean App Platform:")
    print("1. Go to your app → Settings → Environment Variables")
    print("2. REMOVE or comment out: DATABASE_URL")
    print("3. ADD: DIGITALOCEAN_DATABASE_URL")
    print("4. Value format:")
    print("   postgresql://doadmin:PASSWORD@HOST:PORT/database?sslmode=require")
    
    print("\n📋 Step 4: Deploy and Test")
    print("1. Commit your changes:")
    print("   git add .")
    print("   git commit -m 'Switch to DigitalOcean database'")
    print("   git push origin main")
    print("2. After deployment, run:")
    print("   python fix_database_ssl.py")
    
    print("\n🚀 Quick Alternative: Use SQLite")
    print("If you want to test immediately:")
    print("1. Remove ALL database environment variables")
    print("2. Redeploy your app")
    print("3. App will use SQLite (good for testing)")
    
    print("\n💰 Cost: $15/month for DigitalOcean managed database")
    print("✅ Benefits: No SSL issues, managed backups, same provider")

def check_current_config():
    """Check current database configuration"""
    print("\n🔍 Current Database Configuration:")
    print("-" * 40)
    
    if os.getenv('DATABASE_URL'):
        db_url = os.getenv('DATABASE_URL')
        if 'render.com' in db_url:
            print("❌ Currently using Render.com database")
            print("   This is causing SSL connection issues")
        else:
            print("✅ Using non-Render.com database")
    else:
        print("ℹ️  No DATABASE_URL found")
    
    if os.getenv('DIGITALOCEAN_DATABASE_URL'):
        print("✅ DIGITALOCEAN_DATABASE_URL is set")
        print("   App will use DigitalOcean managed database")
    else:
        print("ℹ️  DIGITALOCEAN_DATABASE_URL not set")
        print("   App will use SQLite (development mode)")

if __name__ == '__main__':
    show_database_setup_instructions()
    check_current_config()
