import pandas as pd
import numpy as np
from django.shortcuts import render
from django.http import JsonResponse
from dashboard.models import Equipment
# Import from the root level service module now that the file exists
from services.prediction_service import PredictiveMaintenanceEngine

def live_ml_diagnostics(request):
    """
    Computes real-time analytical health calculations across machinery metrics.
    """
    equipments = Equipment.objects.all()
    ml_engine = PredictiveMaintenanceEngine()
    
    # Generate mock training framework dataframe to initialize the scikit-learn model
    np.random.seed(42)
    training_data = {
        'temperature': np.random.normal(75, 5, 200),
        'pressure': np.random.normal(30, 2, 200),
        'vibration': np.random.normal(1.5, 0.4, 200),
        'rpm': np.random.normal(1500, 50, 200)
    }
    df_train = pd.DataFrame(training_data)
    ml_engine.train_anomaly_detector(df_train)
    
    diagnostic_results = []
    
    for eq in equipments:
        # Create different sensor signatures depending on machine health status
        if eq.health_status == "CRITICAL":
            current_sensors = {'temperature': 98.4, 'pressure': 34.1, 'vibration': 5.2, 'rpm': 1410.0}
        elif eq.health_status == "WARNING":
            current_sensors = {'temperature': 86.1, 'pressure': 31.8, 'vibration': 3.1, 'rpm': 1485.0}
        else:
            current_sensors = {'temperature': 74.2, 'pressure': 29.5, 'vibration': 1.4, 'rpm': 1502.0}
            
        analysis = ml_engine.analyze_current_telemetry(current_sensors)
        
        diagnostic_results.append({
            'equipment': eq,
            'sensors': current_sensors,
            'metrics': analysis
        })
        
    return render(request, 'predictive/diagnostics.html', {'results': diagnostic_results})