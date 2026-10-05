# SimpleGraphics.py
""" A module that supports the simple drawing of colored
rectangles, disks, stars, line segments, and text. """

import matplotlib.pyplot as plt
import numpy as np
from time import sleep as pause

# Built-in SimpleGraphics colors
YELLOW    = [1.0, 1.0, 0.0]
CYAN      = [0.0, 1.0, 1.0]
MAGENTA   = [1.0, 0.0, 1.0]
RED       = [1.0, 0.0, 0.0]
GREEN     = [0.0, 1.0, 0.0]
BLUE      = [0.0, 0.0, 1.0]
WHITE     = [1.0, 1.0, 1.0]
BLACK     = [0.0, 0.0, 0.0]
PURPLE    = [0.57, 0.17, 0.93]
DARKGRAY  = [0.33, 0.33, 0.33]
LIGHTGRAY = [0.67, 0.67, 0.67]
ORANGE    = [1.0, 0.50, 0.0]
PINK      = [1.0, 0.71, 0.80]


def MakeWindow(M, labels=True, bgcolor=WHITE):
    """
    Creates a window with x range -M<=x<=M and y range -M<=y<=M
    """
    M = int(M)

    plt.figure(figsize=(8, 8), dpi=80)

    ticks = np.linspace(-M, M, 2 * M + 1)
    plt.xticks(ticks)
    plt.yticks(ticks)

    plt.xlim(-M, M)
    plt.ylim(-M, M)

    axes = plt.gca()
    axes.set_facecolor(bgcolor)  # <-- Fixed here for modern matplotlib

    if not labels:
        axes.set_xticks([])
        axes.set_yticks([])

    axes.set_aspect('equal', adjustable='box')


def ShowWindow(duration=None):
    """
    Display the current window.
    """
    if duration is None:
        plt.show()
    else:
        plt.show(block=False)
        pause(duration)


def CloseWindow():
    """ Close all windows. """
    plt.close('all')


def DrawRect(a, b, L, W, theta=0.0, FillColor=None,
             EdgeColor=BLACK, EdgeWidth=1):

    L = float(L)
    W = float(W)
    theta = np.deg2rad(theta)

    x0 = np.array([-L/2, L/2, L/2, -L/2, -L/2])
    y0 = np.array([-W/2, -W/2, W/2, W/2, -W/2])

    x = a + np.cos(theta) * x0 - np.sin(theta) * y0
    y = b + np.sin(theta) * x0 + np.cos(theta) * y0

    if FillColor is None:
        plt.plot(x, y, color=EdgeColor, linewidth=EdgeWidth)
    else:
        plt.fill(x, y, facecolor=FillColor,
                 edgecolor=EdgeColor, linewidth=EdgeWidth)


def DrawDisk(a, b, r, FillColor=None, EdgeColor=BLACK, EdgeWidth=1):

    theta = np.linspace(0, 2 * np.pi, 256)
    x = a + r * np.cos(theta)
    y = b + r * np.sin(theta)

    if FillColor is None:
        plt.plot(x, y, color=EdgeColor, linewidth=EdgeWidth)
    else:
        plt.fill(x, y, facecolor=FillColor,
                 edgecolor=EdgeColor, linewidth=EdgeWidth)


def DrawStar(a, b, r, theta=0.0, FillColor=None,
             EdgeColor=BLACK, EdgeWidth=1):

    r2 = r / (2 * (1 + np.sin(np.pi / 10)))
    tau = np.linspace(0, 2 * np.pi, 11) + np.pi / 10 + np.deg2rad(theta)

    x = np.cos(tau)
    y = np.sin(tau)

    x[0::2] *= r
    y[0::2] *= r
    x[1::2] *= r2
    y[1::2] *= r2

    x += a
    y += b

    if FillColor is None:
        plt.plot(x, y, color=EdgeColor, linewidth=EdgeWidth)
    else:
        plt.fill(x, y, facecolor=FillColor,
                 edgecolor=EdgeColor, linewidth=EdgeWidth)


def DrawLineSeg(x0, y0, x1, y1, LineColor=BLACK, LineWidth=1):
    plt.plot([x0, x1], [y0, y1],
             color=LineColor, linewidth=LineWidth)


def DrawText(x, y, s, FontColor=BLACK, FontSize=10):
    plt.text(x, y, s, color=FontColor, fontsize=FontSize)


def Title(s, FontColor=BLACK, FontSize=18):
    plt.title(s, fontsize=FontSize, color=FontColor)


def DrawPoly(x, y, FillColor=None, EdgeWidth=1, EdgeColor=BLACK):

    u = list(x) + [x[0]]
    v = list(y) + [y[0]]

    if FillColor is None:
        plt.plot(u, v, linewidth=EdgeWidth, color=EdgeColor)
    else:
        plt.fill(u, v, facecolor=FillColor,
                 edgecolor=EdgeColor, linewidth=EdgeWidth)