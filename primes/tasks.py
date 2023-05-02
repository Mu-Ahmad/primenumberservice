from __future__ import absolute_import, unicode_literals
from celery import shared_task
import psutil
import datetime
import asyncio, time, threading
from .models import CPUMemoryUsageLog, PrimeNumber

@shared_task
def log_cpu_memory_usage():
    # Get the current time
    current_time = datetime.datetime.now()

    # Get the CPU and memory usage
    cpu_percentages = psutil.cpu_percent(interval=1, percpu=True)
    cpu_usage = sum(cpu_percentages) / len(cpu_percentages)
    memory_info = psutil.virtual_memory()
    memory_usage = 100 - (memory_info.available * 100 / memory_info.total)

    # Create a new CPUMemoryUsageLog object and save it to the database
    log_entry = CPUMemoryUsageLog(timestamp=current_time, cpu_usage=cpu_usage, memory_usage=memory_usage)
    log_entry.save()


@shared_task
def generate_primes(from_num, to_num):
    # Implement prime number generation algorithm here
    # Store prime numbers in database
    for i in range(from_num, to_num+1):
        if is_prime(i):
            try:
                PrimeNumber.objects.create(number=i)
            except Exception as e:
                print(e)

def is_prime(num):
    if num <= 1:
        return False
    for i in range(2, int(num**0.5)+1):
        if num % i == 0:
            return False
    return True


def run_in_background(func, *args):
    """
    Runs a function in the background thread.
    """
    t = threading.Thread(target=func, args=args)
    t.daemon = True
    t.start()

