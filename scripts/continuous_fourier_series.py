import argparse

import matplotlib.pyplot as plt
import numpy as np
from matplotlib.widgets import Slider

T_MAX = 2.0
N_POINTS = 20000


def parse_args():
    parser = argparse.ArgumentParser(description="Continuous Fourier series")
    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument("--square", action="store_true", help="square wave")
    group.add_argument("--saw", action="store_true", help="sawtooth wave")
    return parser.parse_args()


def square_wave(t, n: int, A: float = 1.0, T: float = 1.0, tau: float = 0.5):

    w0 = 2 * np.pi / T
    a0 = A * tau / T
    x = 0

    for k in range(1, n + 1):
        x += (2 * A / (k * np.pi)) * np.sin(k * w0 * tau / 2) * np.cos(k * w0 * t)

    return a0 + x


def sawtooth_wave(t, n: int, A: float = 1.0, T: float = 1.0):

    w0 = 2 * np.pi / T
    x = 0

    for k in range(1, n + 1):
        x += ((-1) ** (k + 1)) * np.sin(k * w0 * t) / k

    return (2 * A / np.pi) * x


def main():
    args = parse_args()
    t = np.linspace(0, T_MAX, N_POINTS)
    fig, ax = plt.subplots()

    k = 10  # default number of harmonics

    if args.square:
        y = square_wave(t, k)
        fig.suptitle("Square Wave, representation with Fourier Series", fontsize=16)
    elif args.saw:
        y = sawtooth_wave(t, k)
        fig.suptitle("Saw Wave, representation with Fourier Series", fontsize=16)

    ax.grid()
    ax.set_xlim(0, T_MAX)
    (line,) = ax.plot(t, y)
    fig.tight_layout()
    fig.subplots_adjust(bottom=0.15)  # room for the slider

    slider_ax = fig.add_axes((0.15, 0.04, 0.7, 0.03))
    k_slider = Slider(slider_ax, "k", 1, 100, valinit=k, valstep=1, initcolor="none")

    def update(val):
        if args.square:
            line.set_ydata(square_wave(t, int(val)))
        elif args.saw:
            line.set_ydata(sawtooth_wave(t, int(val)))
        fig.canvas.draw_idle()

    k_slider.on_changed(update)
    plt.show()


if __name__ == "__main__":
    main()
