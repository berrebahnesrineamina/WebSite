#!/usr/bin/env python3
"""
Test script to verify Django server is working
"""
import requests
import time
import sys

def test_server():
    """Test if the Django server is running and responding"""
    try:
        # Wait a moment for server to start
        time.sleep(3)
        
        # Test the home page
        response = requests.get('http://localhost:8000', timeout=10)
        
        if response.status_code == 200:
            print("✅ Server is running successfully!")
            print(f"Status Code: {response.status_code}")
            print(f"Response Length: {len(response.text)} characters")
            
            # Check if it's the expected page
            if "وثائق+" in response.text or "Wathaiq" in response.text:
                print("✅ Home page content looks correct!")
            else:
                print("⚠️  Home page content might be different than expected")
                
        elif response.status_code == 500:
            print("❌ Server Error (500) - Internal server error")
            print("This is the issue you were experiencing")
        else:
            print(f"⚠️  Unexpected status code: {response.status_code}")
            
    except requests.exceptions.ConnectionError:
        print("❌ Cannot connect to server - is it running?")
        print("Make sure to run: python manage.py runserver")
    except requests.exceptions.Timeout:
        print("❌ Server request timed out")
    except Exception as e:
        print(f"❌ Error testing server: {e}")

if __name__ == '__main__':
    test_server()
