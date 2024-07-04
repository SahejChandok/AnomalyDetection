# Efficient Data Stream Anomaly Detection

## Algorithm: Exponential Moving Average (EMA) and Exponential Moving Standard Deviation (EMSD)

### EMA (Exponential Moving Average)
The EMA gives more weight to recent data points, making it more responsive to recent changes in the data stream. This helps in quickly adapting to changes and trends in the data, which is crucial for real-time anomaly detection.

### EMSD (Exponential Moving Standard Deviation)
The EMSD is used to measure the variability or volatility in the data stream. By calculating the standard deviation of the exponentially weighted data points, we can identify significant deviations from the mean, which are potential anomalies.

### Anomaly Detection
An anomaly is detected if the current data point deviates from the EMA by more than a specified threshold (in terms of EMSD). This threshold is set as a multiple of the EMSD, allowing us to flag data points that are significantly different from the expected range.

### Effectiveness
- **Adaptation to Concept Drift:** The use of EMA and EMSD allows the detector to adapt to gradual changes in the data distribution over time, making it effective in handling concept drift.
- **Handling Seasonal Variations:** By incorporating both seasonal patterns and noise in the data stream generation, the EMA can smooth out these regular fluctuations, while the EMSD helps in detecting true anomalies.
- **Real-time Processing:** The algorithm is computationally efficient, making it suitable for real-time applications where quick detection and response are essential.

### Steps to run the program
- **Navigate to the Directory:** cd ANOMALYDETECTION
- **Install dependencies** pip install -r requirements.txt
- **Run the program** python main.py

