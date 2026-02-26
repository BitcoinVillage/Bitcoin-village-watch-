import random
import time
import json

class WaterSensor:
    def __init__(self, location="Rampur Village"):
        self.location = location
        self.pH_range = (6.0, 8.5)
        self.tds_range = (100, 500)
        self.turbidity_range = (1, 100)
        
    def read_pH(self):
        return round(random.uniform(*self.pH_range), 2)
    
    def read_tds(self):
        return random.randint(*self.tds_range)
    
    def read_turbidity(self):
        return random.randint(*self.turbidity_range)
    
    def detect_contaminants(self):
        # Simulate occasional contamination
        return random.choice([True, False, False, False])
    
    def get_reading(self):
        return {
            "timestamp": time.time(),
            "location": self.location,
            "pH": self.read_pH(),
            "tds": self.read_tds(),
            "turbidity": self.read_turbidity(),
            "contaminants_detected": self.detect_contaminants()
        }

# Test
if __name__ == "__main__":
    sensor = WaterSensor()
    for i in range(5):
        print(json.dumps(sensor.get_reading(), indent=2))
        time.sleep(2)
