from rest_framework import serializers


class RequestSerializer(serializers.Serializer):
    message = serializers.CharField(max_length=10000)
    source = serializers.CharField(max_length=128)
    target = serializers.CharField(max_length=128)
