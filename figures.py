from matplotlib import pyplot as plt
from matplotlib.animation import FuncAnimation
import matplotlib
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure
import numpy as np

matplotlib.use("Qt5Agg")


class FigureProcess(FigureCanvas):
    def __init__(self, dp):
        self.fig = Figure(figsize=(5, 4), dpi=100)
        super(FigureProcess, self).__init__(self.fig)
        self.ax = self.fig.add_subplot(111)

        self.x1, self.y1 = [], []
        self.x2, self.y2 = [], []
        self.lines = self.ax.plot([], [], 'ro', [], [], '--')
        self.ani = FuncAnimation(self.fig, self.figure_update, frames=1000, init_func=self.init_function, interval=50,
                                 blit=True)
        self.dp = dp
        self.temp = []
        self.count = 0

    def init_function(self):
        self.ax.set_xlim(0, 500)
        self.ax.set_ylim(0, 2500)
        return self.lines

    def figure_update(self, frames):
        self.x1 = np.arange(500)
        self.x2 = self.x1
        self.temp = self.dp.current_cache.copy()

        if len(self.dp.current_cache) > 1:
            self.y1 = self.dp.current_cache[0].copy()
        else:
            self.y1 = np.linspace(0, 0, 500)

        if len(self.dp.angle_cache) > 1:
            self.y2 = self.dp.angle_cache[0]
        else:
            self.y2 = np.linspace(0, 0, 500)

        self.lines[0].set_data(self.x1, self.y1)
        self.lines[1].set_data(self.x2, self.y2)
        return self.lines


if __name__ == "__main__":
    pass
