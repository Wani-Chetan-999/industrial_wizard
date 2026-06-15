import numpy as np
import pandas as pd
from sklearn.ensemble import IsolationForest

class PredictiveMaintenanceEngine:
    def __init__(self):
        # Initializing Isolation Forest for Unsupervised Industrial Anomaly Detection
        self.model = IsolationForest(n_estimators=100, contamination=0.05, random_state=42)
        
    def train_anomaly_detector(self, historic_telemetry_df: pd.DataFrame):
        """Expects columns: ['temperature', 'pressure', 'vibration', 'rpm']"""
        features = historic_telemetry_df[['temperature', 'pressure', 'vibration', 'rpm']]
        self.model.fit(features)

    def analyze_current_telemetry(self, current_data: dict) -> dict:
        """
        Analyzes a single sensor payload frame.
        current_data = {'temperature': X, 'pressure': Y, 'vibration': Z, 'rpm': W}
        """
        df = pd.DataFrame([current_data])
        prediction = self.model.predict(df)[0] # 1 = normal, -1 = anomaly
        
        # Simple health generation heuristic mapping out of standard thresholds
        anomaly_score = float(self.model.decision_function(df)[0])
        
        # Calculate dynamic health metric
        base_health = 100
        if current_data['vibration'] > 4.5: base_health -= 30
        if current_data['temperature'] > 95: base_health -= 40
        
        fail_prob = 1.0 - ((anomaly_score + 0.5) / 1.0) # Map to 0-1 probability estimation range
        fail_prob = max(0.0, min(0.99, fail_prob))

        return {
            "is_anomaly": True if prediction == -1 else False,
            "anomaly_score": round(anomaly_score, 4),
            "failure_probability": round(fail_prob, 2),
            "estimated_health": max(10, base_health)
        }