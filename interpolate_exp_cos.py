#! /usr/bin/env python

"""
File: interpolate_exp_cos.py
Copyright (c) 2016 Chinmai Raman
License: MIT
Course: PHYS227
Assignment: B.1
Date: March 17th, 2016
Email: raman105@mail.chapman.edu
Name: Chinmai Raman
Description: Interpolates a discrete function
"""

from __future__ import division
import numpy as np

def f(x):
        return np.exp(-1.0 * x**2) * np.cos(2.0 * np.pi * x)

def discrete_func(a, b, q):
    """
    Computes the value of a function at discrete points and returns the x and y values.
    """
    def f(x):
        return np.exp(-1.0 * x**2) * np.cos(2.0 * np.pi * x)
    x = np.linspace(a, b, q + 1)
    y = f(x)
    return x, y

def S_k(a, b, xp, q):
    """
    Interpolates the function at the points between the discrete points at which the function is evaluated.
    """
    h = (b - a) / float(q)
    k = int((xp - a) / h) + 1
    var = discrete_func(a, b, q)
    return var[1][k] + ((var[1][k + 1] - var[1][k]) / (var[0][k + 1] - var[0][k])) * (xp - var[0][k])

def error(a, b, xp, q):
    """
    Returns the difference between the actual value and the approximation estimated by the interpolation function S_k.
    """
    return abs(f(xp) - S_k(a, b, xp, q))

def test_discrete():
    assert(abs(discrete_func(2)[1][-1] - (1.0 / np.exp(1))) < 1e-6), 'Failure'