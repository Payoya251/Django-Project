import requests

# Hacer la petición a la API
response = requests.get('http://127.0.0.1:8000/api/hello/')

# Mostrar la respuesta formateada
print("Estado de la respuesta:", response.status_code)
print("Respuesta JSON:", response.json())