#! /usr/bin/env python

"""
File: integrate_exp.py
Copyright (c) 2016 Chinmai Raman
License: MIT
Course: PHYS227
Assignment: B.6
Date: March 18th, 2016
Email: raman105@mail.chapman.edu
Name: Chinmai Raman
Description: Uses the trapezoid rule to approximate integration
"""

from __future__ import division
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

def graph():
    fig = plt.figure(1)
    x = np.linspace(-10, 10, 10000)
    y = np.exp(-x**2)
    plt.plot(x, y, 'b-')
    plt.xlabel('x')
    plt.ylabel('y')
    plt.title('f(x)')
    plt.show()

def trap(n, L):
    """
    Implements the trapezoid rule.
    """
    x = np.linspace(0, L, n - 1)
    y = np.exp(-x**2)
    h = L / n
    s = y[0] + y[-1]
    for i in xrange(1, n - 1):
        s += 2 * y[i]
    s *= h / 2 
    return s

def T(n, L):
    """
    Doubles the result of the trapezoid rule.
    """
    return 2 * trap(n, L)

def test_trap():
    assert abs(trap(100, 5) - 0.868502386943) < 1e-6

def table():
    """
    Returns a table of the outputs of double the trapezoid rule at various n and L values.
    """
    data = pd.DataFrame(np.array([T(100, 2), T(100, 4), T(100, 6), T(100, 8), T(100, 10), T(200, 2), T(200, 4), T(200, 6), T(200, 8), T(200, 10), T(300, 2), T(300, 4), T(300, 6), T(300, 8), T(300, 10), T(400, 2), T(400, 4), T(400, 6), T(400, 8), T(400, 10), T(500, 2), T(500, 4), T(500, 6), T(500, 8), T(500, 10)]).reshape((5, 5)), index = ['n = 100', 'n = 200', 'n = 300', 'n = 400', 'n = 500'], columns = ['L = 2', 'L = 4', 'L = 6', 'L = 8', 'L = 10'])
    return data

def error():
    """
    Returns the error from the actual integral value compared to the value calculated by the T function.
    """
    return table() - np.sqrt(np.pi)