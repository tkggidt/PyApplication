from matplotlib import pyplot as plt
from matplotlib.animation import FuncAnimation
import matplotlib
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure
import numpy as np

matplotlib.use("Qt5Agg")


class FigureProcess(FigureCanvas):
    def __init__(self, width=5, height=4, dpi=100):
        self.fig = Figure(figsize=(width, height), dpi=dpi)
        super(FigureProcess, self).__init__(self.fig)
        self.ax = self.fig.add_subplot(111)

        self.x1, self.y1 = [], []
        self.x2, self.y2 = [], []
        self.lines = self.ax.plot([], [], 'ro', [], [], '--')
        self.ani = FuncAnimation(self.fig, self.figure_update, frames=1000, init_func=self.init_function, interval=10,
                                 blit=True)

    def init_function(self):
        self.ax.set_xlim(0, 500)
        self.ax.set_ylim(0, 2500)
        return self.lines

    def figure_update(self, frames):
        self.x1 = np.arange(500)
        self.x2 = self.x1
        self.y1 = np.linspace(0, 2500, 500)
        self.y2 = np.linspace(1000, 0, 500)
        self.lines[0].set_data(self.x1, self.y1 + frames)
        self.lines[1].set_data(self.x2, self.y2)
        return self.lines


if __name__ == "__main__":
    pass
