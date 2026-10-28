import argparse

import matplotlib.pyplot as plt
import numpy as np

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


def main():
    args = parse_args()
    t = np.linspace(0, T_MAX, N_POINTS)
    fig, ax = plt.subplots(figsize=(10, 6))

    if args.square:
        y = square_wave(t, 50)
        fig.suptitle("Square Wave, representation with Fourier Series", fontsize=16)
    elif args.saw:
        print("Sawtooth Wave")

    ax.grid()
    ax.set_xlim(0, T_MAX)
    ax.plot(t, y)
    fig.tight_layout()
    plt.show()


if __name__ == "__main__":
    main()
