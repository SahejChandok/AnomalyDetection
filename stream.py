import numpy as np

def generate_data_stream(window_size):
    while True:
        regular_pattern = np.sin(np.linspace(0, 2 * np.pi, window_size)) * 10
        seasonal_variation = np.sin(np.linspace(0, 8 * np.pi, window_size)) * 5
        noise = np.random.normal(0, 1, window_size)
        data_stream = regular_pattern + seasonal_variation + noise
        data_stream[window_size // 2] += 150  # Injecting an anomaly
        yield data_stream  
