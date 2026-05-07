"""Collection of the core mathematical operators used throughout the code base."""

import math

# ## Task 0.1
from typing import Callable, Iterable

#
# Implementation of a prelude of elementary functions.

# Mathematical functions:
# - mul
def mul(x, y): # type: ignore
    return x*y

# - id
def id(x): # type: ignore
    return x
# - add
def add(x, y): # type: ignore
    return x+y

# - neg
def neg(x): # type: ignore
    return x * -1

# - lt
def lt(x, y): # type: ignore
    return x < y

# - eq
def eq(x, y): # type: ignore
    return x == y

# - max
def max(x, y): # type: ignore
    return x if x > y else y

# - is_close
def is_close(x, y): # type: ignore
    return math.isclose(x, y, abs_tol=1e-2)

# - sigmoid
def sigmoid(x): # type: ignore
    if x >=0:
        return 1 / (1+ math.exp(-x))
    else:
        return math.exp(x)/(1+ math.exp(x))

# - relu
def relu(x): # type: ignore
    return max(0, x)

# - log
def log(x): # type: ignore
    return math.log(x)

# - exp
def exp(x): # type: ignore
    return math.exp(x)

# - log_back
def log_back(x, y): # type: ignore
    return (1/x) * y

# - inv
def inv(x): # type: ignore
    return 1/x

# - inv_back
def inv_back(x, y): # type: ignore
    return (-1/x**2) * y

# - relu_back
def relu_back(x , y): # type: ignore
    return (x >= 0) * y
#
# For sigmoid calculate as:
# $f(x) =  \frac{1.0}{(1.0 + e^{-x})}$ if x >=0 else $\frac{e^x}{(1.0 + e^{x})}$
# For is_close:
# $f(x) = |x - y| < 1e-2$


# TODO: Implement for Task 0.1.


# ## Task 0.3

# Small practice library of elementary higher-order functions.

# Implement the following core functions
# - map
def map(fn): # type: ignore
    def apply(xs : Iterable[float]):
        return [fn(x) for x in xs]
    return apply

# - zipWith
def zipWith(fn): # type: ignore
    def apply(xs: Iterable[float], ys: Iterable[float]):
        return [fn(x,y) for x , y in zip(xs, ys)]
    return apply

# - reduce
def reduce(fn, start):  # type: ignore
    def apply(xs : Iterable[float]):
        res = start
        for x in xs:
            res = fn(res,x)
        return res
    return apply

#
# Use these to implement

# - negList : negate a list
def negList(xs : Iterable[float]):
    return map(neg)(xs)

# - addLists : add two lists together
def addLists(xs: Iterable[float], ys: Iterable[float]):
    return zipWith(add)(xs, ys)

# - sum: sum lists
def sum(xs: Iterable[float]):
    return reduce(add, 0.0)(xs)

# - prod: take the product of lists
def prod(xs: Iterable[float]):
    return reduce(mul, 1.0)(xs)
# TODO: Implement for Task 0.3.
