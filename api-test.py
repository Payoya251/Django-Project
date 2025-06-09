import requests

def square_root(number):

    response = requests.get(
        'http://127.0.0.1:8000/api/square-root/',
        params={'number': number}
    )
    return response.json()['result']

if __name__ == "__main__":

    print(square_root(64))