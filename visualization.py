import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

class RealTimePlot:
    def __init__(self):
        self.fig, self.ax = plt.subplots()
        self.x_data, self.y_data = [], []
        self.line, = self.ax.plot([], [], 'b-')
        self.anomaly_dots, = self.ax.plot([], [], 'ro')

    def init_plot(self):
        self.ax.set_xlim(0, 100)
        self.ax.set_ylim(-2, 2)
        return self.line, self.anomaly_dots

    def update_plot(self, new_data):
        x, y, is_anomaly = new_data
        self.x_data.append(x)
        self.y_data.append(y)
        
        if is_anomaly:
            self.anomaly_dots.set_data(self.x_data[-1:], self.y_data[-1:])

        self.line.set_data(self.x_data, self.y_data)
        return self.line, self.anomaly_dots

    def animate(self, data_generator):
        animation = FuncAnimation(self.fig, self.update_plot, data_generator, init_func=self.init_plot, blit=True)
        plt.show()
