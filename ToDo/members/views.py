from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .serializers import SquareRootSerializer
import math

# Regular Django view
@api_view(['GET'])
def members(request):
    return Response({"message": "Welcome to the Api"})

@api_view(['GET'])
def calculate_square_root(request):

    number = float(request.query_params.get('number'))
        
    result = math.sqrt(number)
    data = {
        'number': number,
        'result': result
    }
    serializer = SquareRootSerializer(instance=data)
    return Response(serializer.data)
