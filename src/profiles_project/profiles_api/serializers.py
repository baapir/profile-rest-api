from rest_framework import serializers


class HelloSerializer(serializers.Serializer):
    """serializers a name field for testing ou APIView"""

    name = serializers.CharField(max_length=10)
