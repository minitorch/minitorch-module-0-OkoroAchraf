import math
import random
from dataclasses import dataclass
from typing import List, Tuple


def make_pts(N):
    "This function makes N random (x1, x2) points"
    X = []
    for i in range(N):
        x_1 = random.random()
        x_2 = random.random()
        X.append((x_1, x_2))
    return X


@dataclass
class Graph:
    N: int
    X: List[Tuple[float, float]]
    y: List[int]


def simple(N):
    "This function makes N random (x1, x2) points. It then "
    "assigns a Y output to the x1's . If x1 <0.5 then the Y given is 1"
    "else the Y is 0"
    X = make_pts(N)
    y = []
    for x_1, x_2 in X:
        y1 = 1 if x_1 < 0.5 else 0
        y.append(y1)
    return Graph(N, X, y)


def diag(N):
    "This function makes N random (x1, x2) points. It then "
    "assigns a Y output to the points. If x1+x2 <0.5 then the Y given is 1"
    "else the Y is 0"
    X = make_pts(N)
    y = []
    for x_1, x_2 in X:
        y1 = 1 if x_1 + x_2 < 0.5 else 0
        y.append(y1)
    return Graph(N, X, y)


def split(N):
    "This function makes N random (x1, x2) points. It then "
    "assigns a Y output to the x1's . If x1 <0.2 or > 0.8 then the Y given is 1"
    "else the Y is 0"
    X = make_pts(N)
    y = []
    for x_1, x_2 in X:
        y1 = 1 if x_1 < 0.2 or x_1 > 0.8 else 0
        y.append(y1)
    return Graph(N, X, y)


def xor(N):
    "This function makes N random (x1, x2) points. It then "
    "assigns a Y output to the ponts. If x_1 < 0.5 and x_2 > 0.5 or x_1 > 0.5 and x_2 < 0.5"
    "then the Y given is 1 else the Y is 0"
    X = make_pts(N)
    y = []
    for x_1, x_2 in X:
        y1 = 1 if x_1 < 0.5 and x_2 > 0.5 or x_1 > 0.5 and x_2 < 0.5 else 0
        y.append(y1)
    return Graph(N, X, y)


def circle(N):
    "This function makes N random (x1, x2) points. It then "
    "assigns a Y output based on distance from the center (0.5, 0.5). "
    "If the squared distance is > 0.1 (outside the circle) the Y given is 1, "
    "else (inside the circle) the Y is 0."
    X = make_pts(N)
    y = []
    for x_1, x_2 in X:
        x1, x2 = x_1 - 0.5, x_2 - 0.5
        y1 = 1 if x1 * x1 + x2 * x2 > 0.1 else 0
        y.append(y1)
    return Graph(N, X, y)


def spiral(N):
    "This function makes N points arranged in two interleaved spiral arms "
    "centered at (0.5, 0.5). The first N//2 points form one arm with Y=0, "
    "the remaining N//2 points form a second arm rotated 90 degrees with Y=1. "
    "The arms are parameterized by t in [0, 10] using x(t) = t*cos(t)/20 and "
    "y(t) = t*sin(t)/20."
    def x(t):
        return t * math.cos(t) / 20.0

    def y(t):
        return t * math.sin(t) / 20.0
    X = [(x(10.0 * (float(i) / (N // 2))) + 0.5, y(10.0 * (float(i) / (N //
        2))) + 0.5) for i in range(5 + 0, 5 + N // 2)]
    X = X + [(y(-10.0 * (float(i) / (N // 2))) + 0.5, x(-10.0 * (float(i) /
        (N // 2))) + 0.5) for i in range(5 + 0, 5 + N // 2)]
    y2 = [0] * (N // 2) + [1] * (N // 2)
    return Graph(N, X, y2)


datasets = {'Simple': simple, 'Diag': diag, 'Split': split, 'Xor': xor,
    'Circle': circle, 'Spiral': spiral}
