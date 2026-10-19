# signals-lab

A visual companion for working through Alan V. Oppenheim's classic textbooks on signals and systems and discrete-time signal processing.

Each notebook takes a topic from the books and turns it into something you can see and play with: the formula, the code that implements it, and the plot it produces, side by side. The goal is not to replace the books but to make their mathematics tangible — to check every derivation numerically and to build intuition for what the equations are actually doing.

## Reference textbooks

| Book | Authors | Focus |
|---|---|---|
| *Signals and Systems* | Alan V. Oppenheim, Alan S. Willsky | Continuous- and discrete-time signals, LTI systems, Fourier analysis, Laplace and Z-transforms |
| *Discrete-Time Signal Processing* | Alan V. Oppenheim, Ronald W. Schafer | Sampling, the DFT and FFT, filter design, spectral analysis |

The notebooks follow the books topic by topic. Chapter numbers differ between editions, so each notebook names the topic it covers rather than a chapter number.

## Notation

This repository uses the convention taught at UPM (Universidad Politécnica de Madrid), which differs from *Discrete-Time Signal Processing*:

| Symbol | Meaning | Units |
|---|---|---|
| $\omega$ | Angular frequency, continuous time | rad/s |
| $\Omega$ | Angular frequency, discrete time | rad/sample |
| $f_s$ | Sampling frequency | Hz |
| $T_s = 1/f_s$ | Sampling period | s |

The two are related by sampling:

$$\Omega = \omega T_s = 2\pi \frac{f}{f_s}$$

*Signals and Systems* uses this same convention. *Discrete-Time Signal Processing* swaps the two letters, so formulas taken from it are translated.


## Getting started

The project is managed with [uv](https://docs.astral.sh/uv/).

```bash
git clone <repository-url> signals-lab
cd signals-lab
uv sync
uv run jupyter lab
```

Notebooks can also be opened directly in VS Code with the Python and Jupyter extensions: select the project's `.venv` as the kernel.

## Dependencies

| Library | Role |
|---|---|
| NumPy | Arrays, complex numbers, FFT |
| SciPy (`scipy.signal`) | Convolution, filters, frequency response, LTI systems |
| Matplotlib | Plots: `plot` for continuous time, `stem` for discrete time |
| SymPy | Symbolic integrals and transforms, to check derivations exactly |
| JupyterLab, ipywidgets | Interactive notebooks with sliders |