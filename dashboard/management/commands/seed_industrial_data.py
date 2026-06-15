from django.core.management.base import BaseCommand
from dashboard.models import Equipment
from alerts.models import Alert

class Command(BaseCommand):
    help = 'Seeds initial telemetry records and structural asset models for the hackathon deployment.'

    def handle(self, *args, **kwargs):
        # 1. Clear out historical records cleanly to avoid relational collisions
        Alert.objects.all().delete()
        Equipment.objects.all().delete()

        # 2. Re-create the master industrial equipment nodes explicitly
        eq1 = Equipment.objects.create(
            equipment_id="BF-001",
            name="Blast Furnace Oxygen Feed Pump",
            type="Blast Furnace Component",
            criticality="CRITICAL",
            health_status="HEALTHY",
            health_percentage=94
        )
        
        eq2 = Equipment.objects.create(
            equipment_id="RM-042",
            name="Hot Rolling Mill Finish Stand Section 4",
            type="Rolling Mill Drive Train",
            criticality="HIGH",
            health_status="WARNING",
            health_percentage=62
        )

        eq3 = Equipment.objects.create(
            equipment_id="CONV-10",
            name="Coke Ore Supply Line Conveyor Engine",
            type="Material Handling Systems",
            criticality="MEDIUM",
            health_status="CRITICAL",
            health_percentage=28
        )

        # 3. Create dependent alerts by passing the direct object instance
        Alert.objects.create(
            equipment=eq2,
            alert_type="Bearing Temperature Spike",
            severity="WARNING",
            message="Structural bearing temp registered at 92°C, crossing nominal limit of 85°C."
        )

        Alert.objects.create(
            equipment=eq3,
            alert_type="Structural Vibration Anomaly",
            severity="CRITICAL",
            message="Velocity breakdown: Anomaly detection model flagged severe unbalance signature along axis-Y."
        )

        self.stdout.write(self.style.SUCCESS('Successfully seeded Steel Plant Operations Matrix!'))