from django.db import models
from django.contrib.auth.models import User

class Equipment(models.Model):
    CRITICALITY_CHOICES = [
        ('LOW', 'Low Operational Risk'),
        ('MEDIUM', 'Medium Process Risk'),
        ('HIGH', 'High Line Stop Risk'),
        ('CRITICAL', 'Plant Shutdown Risk'),
    ]
    STATUS_CHOICES = [
        ('HEALTHY', 'Healthy'),
        ('WARNING', 'Warning'),
        ('CRITICAL', 'Critical Alert'),
    ]
    equipment_id = models.CharField(max_length=50, unique=True)
    name = models.CharField(max_length=100)
    type = models.CharField(max_length=100) # Blast Furnace, Hot Rolling, Conveyor
    location = models.CharField(max_length=100)
    criticality = models.CharField(max_length=20, choices=CRITICALITY_CHOICES, default='MEDIUM')
    health_status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='HEALTHY')
    health_percentage = models.IntegerField(default=100)

    def __str__(self):
        return f"{self.name} ({self.equipment_id})"

class SensorData(models.Model):
    equipment = models.ForeignKey(Equipment, on_delete=models.CASCADE, related_name='telemetry')
    timestamp = models.DateTimeField(auto_now_add=True)
    temperature = models.FloatField()
    pressure = models.FloatField()
    vibration = models.FloatField()
    rpm = models.FloatField()

    class Meta:
        ordering = ['-timestamp']