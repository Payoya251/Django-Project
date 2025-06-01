import requests
import json

try:
    # Make the API request
    response = requests.get('http://127.0.0.1:8000/api/hello/')
    
    # Print status code
    print(f"Status Code: {response.status_code}")
    
    # Try to parse and print JSON response
    try:
        json_response = response.json()
        print("Response JSON:")
        print(json.dumps(json_response, indent=2))
    except ValueError:
        print("Response (not JSON):")
        print(response.text)
        
except requests.exceptions.RequestException as e:
    print(f"Error making request: {e}")