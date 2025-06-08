import requests

def test_square_root(number):

    try:

        response = requests.get(
            'http://127.0.0.1:8000/api/square-root/',
            params={'number': number}
        )

        print(f"Square root of {number} is: {response.json()['result']}")
            
    except requests.exceptions.RequestException as e:
        print(f"Request Error: {e}")

if __name__ == "__main__":
    
    test_square_root(4)