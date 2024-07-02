from stream import generate_data_stream
from anomaly_detection import ZScoreDetector
from visualization import RealTimePlot

def data_generator(detector, stream):
    for x, value in enumerate(stream):
        is_anomaly = detector.detect(value)
        yield x, value, is_anomaly

if __name__ == "__main__":
    stream = generate_data_stream()
    detector = ZScoreDetector()
    plot = RealTimePlot()

    plot.animate(lambda: data_generator(detector, stream))
