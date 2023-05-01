from django.db import models

class CPUMemoryUsageLog(models.Model):
    timestamp = models.DateTimeField()
    cpu_usage = models.FloatField()
    memory_usage = models.FloatField()


class PrimeNumber(models.Model):
    number = models.IntegerField(unique=True)