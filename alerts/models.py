from django.db import models

class Alert(models.Model):
    SEVERITY_CHOICES = [
        ('WARNING', 'Warning'),
        ('CRITICAL', 'Critical'),
    ]
    
    # Ensure this exact field is present
    equipment = models.ForeignKey(
        'dashboard.Equipment', 
        on_delete=models.CASCADE, 
        related_name='alerts'
    )
    alert_type = models.CharField(max_length=100) 
    severity = models.CharField(max_length=20, choices=SEVERITY_CHOICES)
    message = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)
    is_resolved = models.BooleanField(default=False)

    class Meta:
        ordering = ['-timestamp']

    def __str__(self):
        return f"[{self.severity}] {self.equipment.name} - {self.alert_type}"