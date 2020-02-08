from matplotlib import pyplot as plt
from matplotlib.animation import FuncAnimation
import numpy as np


class FigureProcess:
    def __init__(self):
        self.count = 0
        self.fig, self.ax = plt.subplots()
        self.x1, self.y1 = [], []
        self.x2, self.y2 = [], []
        self.lines = self.ax.plot([], [], 'ro', [], [], '--')
        self.ani = FuncAnimation(self.fig, self.update, frames=100, init_func=self.init_function, blit=True)

    def show_figure(self):
        plt.show()

    def init_function(self):
        self.ax.set_xlim(0, 500)
        self.ax.set_ylim(0, 2500)
        return self.lines

    def update(self, steps):
        self.x1 = np.arange(500)
        self.x2 = self.x1
        self.y1 = np.linspace(0, 2500, 500)
        self.y2 = np.linspace(1000, 0, 500)
        self.lines[0].set_data(self.x1, self.y1)
        self.lines[1].set_data(self.x2, self.y2)
        return self.lines


if __name__ == "__main__":
    fp = FigureProcess()
    fp.show_figure()
