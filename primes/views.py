from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import CPUMemoryUsageLog, PrimeNumber
from .serializers import CPUMemoryUsageLogSerializer, PrimeNumberSerializer
from .tasks import generate_primes, run_in_background
import time

@api_view((['Get']))
def monitor(request):
	k = int(request.GET.get('k'))
	log = CPUMemoryUsageLog.objects.all().order_by('-id')[:k]
	serializer = CPUMemoryUsageLogSerializer(log, many=True)
	return Response(serializer.data)

@api_view(['Get'])
def generate(request):
    from_num = int(request.POST.get('from'))
    to_num = int(request.POST.get('to'))
    # curr = generate_primes.delay(from_num, to_num) # starting a background job
    run_in_background(generate_primes, from_num, to_num) # starting a background job
    return Response({'status': 'Success'})

@api_view(['Get'])
def get(request):
	nums = PrimeNumber.objects.all().order_by('number')
	serializer = PrimeNumberSerializer(nums, many=True)
	return Response(serializer.data)