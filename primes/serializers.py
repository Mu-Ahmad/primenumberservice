from rest_framework import serializers
from .models import CPUMemoryUsageLog, PrimeNumber

class CPUMemoryUsageLogSerializer(serializers.ModelSerializer):
    class Meta:
        model = CPUMemoryUsageLog
        # fields = '__all__'
        exclude = ('id',) 

class PrimeNumberSerializer(serializers.ModelSerializer):
    class Meta:
        model = PrimeNumber
        # fields = '__all__'
        exclude = ('id',) 