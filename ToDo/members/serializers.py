from rest_framework import serializers

class MessageSerializer(serializers.Serializer):
    message = serializers.CharField()
    framework = serializers.CharField()
    user = serializers.CharField(required=False)  # Made optional since it has a default value
