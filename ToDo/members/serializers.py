from rest_framework import serializers

class SquareRootSerializer(serializers.Serializer):
    number = serializers.FloatField(min_value=0)
    result = serializers.FloatField(required=False)
