import numpy as np

class ZScoreDetector:
    def __init__(self, threshold=3, window_size=100):
        self.threshold = threshold
        self.window_size = window_size
        self.data = []

    def detect(self, value):
        self.data.append(value)
        if len(self.data) > self.window_size:
            self.data.pop(0)

        mean = np.mean(self.data)
        std_dev = np.std(self.data)
        
        if std_dev == 0:
            return False

        z_score = (value - mean) / std_dev
        return abs(z_score) > self.threshold
