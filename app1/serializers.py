from importlib.metadata import requires
from rest_framework import serializers
class CalculatorSerializers(serializers.Serializer):
    num1 = serializers.IntegerField(required = True)
    num2 = serializers.IntegerField(required = True)
    opr = serializers.CharField(max_length = 3 , required = True)