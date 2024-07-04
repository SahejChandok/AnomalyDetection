import matplotlib.pyplot as plt

def visualize_data_stream(data_stream_generator, anomaly_detector, total_points):
    plt.ion()
    fig, ax = plt.subplots()
    x_data = []
    y_data = []
    anomaly_data = []

    for i, data_window in enumerate(data_stream_generator):
        if len(x_data) >= total_points:
            break

        x_data.extend(range(len(x_data), len(x_data) + len(data_window)))
        y_data.extend(data_window)

        for j, value in enumerate(data_window):
            is_anomaly, anomaly_value = anomaly_detector.detect_anomaly(value)
            if is_anomaly:
                anomaly_data.append((len(x_data) - len(data_window) + j, anomaly_value))

        ax.clear()
        ax.plot(x_data, y_data, label='Data Stream')
        if anomaly_data:
            ax.scatter(*zip(*anomaly_data), color='r', label='Anomalies')
        ax.legend()
        ax.set_title('Real-time Data Stream Anomaly Detection')
        ax.set_xlabel('Time')
        ax.set_ylabel('Value')
        plt.pause(0.01)  

    plt.ioff()
    plt.show()

