#!/usr/bin/env python3
import requests
import json

# Test the API endpoints
base_url = "http://localhost:8080"

# Create a session to maintain cookies
session = requests.Session()

print("1. Testing home page...")
response = session.get(f"{base_url}/")
print(f"   Status: {response.status_code}")

print("\n2. Testing determine_blocks...")
response = session.post(f"{base_url}/determine_blocks", data={
    'product_for_LEAs': 'no',
    'uses_personal_data': 'yes', 
    'uses_AI': 'no'
})
print(f"   Status: {response.status_code}")
print(f"   Response: {response.text}")

print("\n3. Testing question endpoint...")
response = session.get(f"{base_url}/question")
print(f"   Status: {response.status_code}")
print(f"   Response: {response.text}")