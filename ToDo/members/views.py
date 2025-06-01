from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import MessageSerializer

# Regular Django view
@api_view(['GET'])
def members(request):
    return Response({"message": "Hello World!"})

# API View using DRF
@api_view(['GET'])
def api_hello(request):
    message = {
        'message': 'Helloooooo',
        'framework': 'Django REST framework',
        'user': 'anonymous'  # Adding user field to match the serializer
    }
    serializer = MessageSerializer(message)
    return Response(serializer.data)