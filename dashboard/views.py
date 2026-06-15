from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from dashboard.models import Equipment, SensorData
from alerts.models import Alert

# For hackathon testing, we temporarily waive formal login blocks if desired,
# but using the decorator guarantees clean role routing.
def dashboard_home(request):
    equipments = Equipment.objects.all()
    recent_alerts = Alert.objects.filter(is_resolved=False)[:5]
    
    # Pack initial mock dataset lists for structural graph streams
    chart_labels = ["04:00", "08:00", "12:00", "16:00", "20:00", "24:00"]
    temp_trend = [72, 78, 85, 91, 88, 74]
    vibe_trend = [1.2, 1.5, 2.8, 4.9, 3.2, 1.4] # Simulated vibration spike at 16:00

    context = {
        'equipments': equipments,
        'recent_alerts': recent_alerts,
        'chart_labels': chart_labels,
        'temp_trend': temp_trend,
        'vibe_trend': vibe_trend,
    }
    return render(request, 'dashboard/index.html', context)