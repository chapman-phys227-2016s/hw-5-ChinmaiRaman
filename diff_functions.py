#! /usr/bin/env python

"""
File: diff_functions.py
Copyright (c) 2016 Chinmai Raman
License: MIT
Course: PHYS227
Assignment: B.8
Date: March 18th, 2016
Email: raman105@mail.chapman.edu
Name: Chinmai Raman
Description: Plots functions and their derivatives
"""

from __future__ import division
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

def diff(f, a, b, n):
    """
    Finds the derivative of a function at many points.
    """
    x = np.linspace(a, b, n + 1)
    y = np.zeros(len(x))
    z = np.zeros(len(x))
    h = (b - a)/float(n)
    for i in xrange(len(x)):
        y[i] = f(x[i])
    for i in xrange(len(x) - 1):
        z[i] = (y[i + 1] - y[i]) / h
    z[n] = (y[n] - y[n - 1]) / h
    return z

def f(x):
    return np.log(x + 1/100)

def g(x):
    return np.cos(np.exp(10 * x))

def h(x):
    return x**x

def fprime(x):
    return 1 / (x + (1 / 100))

def gprime(x):
    return -10 * np.exp(10 * x) * np.sin(np.exp(10 * x))

def hprime(x):
    return (np.log(x)) * x**x + x * x**(x - 1)

def graph(der):
    fig = plt.figure(1)
    x = np.linspace(1/1000, 1, 101)
    y = der
    plt.plot(x, y, 'b-')
    plt.xlabel('x')
    plt.ylabel('y')
    plt.show()

def multigraph(der, prime):
    """
    Graphs the analytical and discrete derivatives of a function.
    """
    fig = plt.figure(1)
    x = np.linspace(1/1000, 1, 101)
    y1 = der
    y2 = prime(x)
    plt.plot(x, y1, 'b-')
    plt.plot(x, y2, 'r-')
    plt.xlabel('x')
    plt.ylabel('y')
    plt.title('Analytical vs Discrete derivatives')
    plt.show()