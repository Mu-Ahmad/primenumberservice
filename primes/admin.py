from django.contrib import admin
from .models import CPUMemoryUsageLog, PrimeNumber

# Register your models here.
admin.site.register(CPUMemoryUsageLog)
admin.site.register(PrimeNumber)