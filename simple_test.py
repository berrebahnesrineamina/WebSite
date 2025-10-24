#!/usr/bin/env python3
"""
Simple test to check if Django server is working
"""
import urllib.request
import urllib.error
import time

def test_server():
    """Test if the Django server is responding"""
    try:
        # Wait for server to start
        time.sleep(2)
        
        # Test the home page
        response = urllib.request.urlopen('http://localhost:8000', timeout=10)
        
        if response.getcode() == 200:
            print("✅ Server is running successfully!")
            print(f"Status Code: {response.getcode()}")
            
            # Read a bit of content
            content = response.read(500).decode('utf-8')
            print(f"Content preview: {content[:100]}...")
            
        else:
            print(f"⚠️  Unexpected status code: {response.getcode()}")
            
    except urllib.error.URLError as e:
        print(f"❌ Cannot connect to server: {e}")
        print("Make sure the server is running with: python manage.py runserver")
    except Exception as e:
        print(f"❌ Error testing server: {e}")

if __name__ == '__main__':
    test_server()
