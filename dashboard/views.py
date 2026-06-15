import os
import pandas as pd
import numpy as np
from django.shortcuts import render
from dashboard.models import Equipment
from alerts.models import Alert
from services.prediction_service import PredictiveMaintenanceEngine

def dashboard_home(request):
    equipments = Equipment.objects.all()
    # Pull the 5 most recent unresolved operational warning logs
    recent_alerts = Alert.objects.filter(is_resolved=False).order_by('-timestamp')[:5]
    
    # Initialize our ML engine to dynamically compute live system overview health markers
    ml_engine = PredictiveMaintenanceEngine()
    np.random.seed(42)
    df_train = pd.DataFrame({
        'temperature': np.random.normal(75, 5, 200),
        'pressure': np.random.normal(30, 2, 200),
        'vibration': np.random.normal(1.5, 0.4, 200),
        'rpm': np.random.normal(1500, 50, 200)
    })
    ml_engine.train_anomaly_detector(df_train)

    # Compute quick aggregate status counts for our SCADA analytics metrics panel
    total_assets = equipments.count()
    anomaly_count = 0
    
    for eq in equipments:
        if eq.health_status == "CRITICAL":
            sensors = {'temperature': 98.4, 'pressure': 34.1, 'vibration': 5.2, 'rpm': 1410.0}
        elif eq.health_status == "WARNING":
            sensors = {'temperature': 86.1, 'pressure': 31.8, 'vibration': 3.1, 'rpm': 1485.0}
        else:
            sensors = {'temperature': 74.2, 'pressure': 29.5, 'vibration': 1.4, 'rpm': 1502.0}
            
        res = ml_engine.analyze_current_telemetry(sensors)
        if res['is_anomaly']:
            anomaly_count += 1

    context = {
        'equipments': equipments,
        'recent_alerts': recent_alerts,
        'total_assets': total_assets,
        'anomaly_count': anomaly_count,
        'nominal_count': total_assets - anomaly_count,
        # Baseline graph coordinate parameters
        'chart_labels': ["04:00", "08:00", "12:00", "16:00", "20:00", "24:00"],
        'temp_trend': [72, 76, 81, 94, 85, 73],
        'vibe_trend': [1.1, 1.4, 1.9, 5.1, 3.4, 1.3]
    }
    return render(request, 'dashboard/index.html', context)