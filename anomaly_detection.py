import numpy as np

class EMAAnomalyDetector:
    def __init__(self, alpha, threshold):
        self.alpha = alpha
        self.threshold = threshold
        self.ema = None
        self.emsd = None
        self.squared_ema = None
    
    def detect_anomaly(self, new_value):
        if self.ema is None:
            # Initialize EMA and squared EMA
            self.ema = new_value
            self.squared_ema = new_value ** 2
            return False, None
        
        # Update EMA and squared EMA
        self.ema = self.alpha * new_value + (1 - self.alpha) * self.ema
        self.squared_ema = self.alpha * (new_value ** 2) + (1 - self.alpha) * self.squared_ema
        
        # Calculate EMSD
        self.emsd = np.sqrt(self.squared_ema - self.ema ** 2)
        
        # Detect anomaly
        if abs(new_value - self.ema) > (self.emsd * self.threshold): 
            print(f"Anomaly detected: Value={new_value}, EMA={self.ema}, EMSD={self.emsd}")
            return True, new_value
        return False, None
