from stream import generate_data_stream
from anomaly_detection import EMAAnomalyDetector
from visualization import visualize_data_stream

def main():
    window_size = 100
    alpha = 0.3  # Smoothing factor for EMA
    threshold = 1.5  # Number of standard deviations for anomaly detection
    total_points = 500  # Total number of data points to process

    data_stream = generate_data_stream(window_size)
    anomaly_detector = EMAAnomalyDetector(alpha, threshold)
    visualize_data_stream(data_stream, anomaly_detector, total_points)

if __name__ == "__main__":
    main()
