#! /usr/bin/env python

"""
File: plot_sin_eps.py
Copyright (c) 2016 Chinmai Raman
License: MIT
Course: PHYS227
Assignment: B.2
Date: March 17th, 2016
Email: raman105@mail.chapman.edu
Name: Chinmai Raman
Description: Studies a function for different parameter values
"""

from __future__ import division
import numpy as np
import matplotlib.pyplot as plt

def sin_graph(eps, n):
    fig = plt.figure(1)
    x = np.linspace(0, 1, n + 1)
    y = np.sin(1 / (x + eps))
    plt.plot(x, y, 'b-')
    plt.xlabel('x')
    plt.ylabel('y')
    plt.title('f(x)')
    plt.axis([-0.2, 1.2, -1.2, 1.2])
    plt.show()
    
def multigraph(eps, n1):
    n2 = n1 + 10
    fig = plt.figure(1)
    x1 = np.linspace(0, 1, n1)
    y1 = np.sin(1 / (x1 + eps))
    x2 = np.linspace(0, 1, n2)
    y2 = np.sin(1 / (x2 + eps))
    plt.plot(x1, y1, 'b-')
    plt.plot(x2, y2, 'r-')
    plt.xlabel('x')
    plt.ylabel('y')
    plt.title('f(x)')
    plt.axis([-0.2, 1.2, -1.2, 1.2])
    plt.show()

def choose_n(eps):
    n1 = 1
    n2 = n1 + 10
    x1 = np.linspace(0, 1, n1)
    y1 = np.sin(1 / (x1 + eps))
    x2 = np.linspace(0, 1, n2)
    y2 = np.sin(1 / (x2 + eps))
    while (abs(max(y2) - max(y1)) >= 0.1):
        n1 += 1
        n2 += 1
        x1 = np.linspace(0, 1, n1)
        y1 = np.sin(1 / (x1 + eps))
        x2 = np.linspace(0, 1, n2)
        y2 = np.sin(1 / (x2 + eps))
    return n1