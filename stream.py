import numpy as np

def generate_data_stream(period=100, noise_level=0.1):
    t = 0
    while True:
        # Regular pattern: sine wave
        value = np.sin(2 * np.pi * t / period)
        # Adding seasonal variation
        value += 0.1 * np.sin(2 * np.pi * t / (period * 10))
        # Adding noise
        value += noise_level * np.random.randn()
        yield value
        t += 1
