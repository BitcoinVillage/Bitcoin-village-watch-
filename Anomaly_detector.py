import json

class AnomalyDetector:
    def __init__(self):
        self.pH_normal = (6.5, 8.0)
        self.tds_normal = (0, 400)
        self.turbidity_normal = (0, 80)
        
    def check_pH(self, value):
        if value < self.pH_normal[0]:
            return "pH_too_low"
        elif value > self.pH_normal[1]:
            return "pH_too_high"
        return "normal"
    
    def check_tds(self, value):
        if value > self.tds_normal[1]:
            return "high_tds"
        return "normal"
    
    def check_turbidity(self, value):
        if value > self.turbidity_normal[1]:
            return "high_turbidity"
        return "normal"
    
    def analyze(self, sensor_data):
        alerts = []
        
        pH_status = self.check_pH(sensor_data.get("pH", 7.0))
        if pH_status != "normal":
            alerts.append(pH_status)
            
        tds_status = self.check_tds(sensor_data.get("tds", 0))
        if tds_status != "normal":
            alerts.append(tds_status)
            
        turbidity_status = self.check_turbidity(sensor_data.get("turbidity", 0))
        if turbidity_status != "normal":
            alerts.append(turbidity_status)
            
        if sensor_data.get("contaminants_detected", False):
            alerts.append("contaminants_found")
            
        return {
            "timestamp": sensor_data.get("timestamp"),
            "location": sensor_data.get("location"),
            "alerts": alerts,
            "status": "ALERT" if alerts else "NORMAL"
        }

# Test
if __name__ == "__main__":
    detector = AnomalyDetector()
    
    # Normal data
    normal_data = {
        "timestamp": 1234567890,
        "location": "Rampur Village",
        "pH": 7.2,
        "tds": 250,
        "turbidity": 45,
        "contaminants_detected": False
    }
    
    # Anomaly data
    anomaly_data = {
        "timestamp": 1234567895,
        "location": "Rampur Village",
        "pH": 5.8,
        "tds": 550,
        "turbidity": 95,
        "contaminants_detected": True
    }
    
    print("Normal:", detector.analyze(normal_data))
    print("Anomaly:", detector.analyze(anomaly_data))
