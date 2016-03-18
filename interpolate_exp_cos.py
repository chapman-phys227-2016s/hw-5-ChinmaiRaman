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
    def f(x):
        return np.exp(-1.0 * x**2) * np.cos(2.0 * np.pi * x)
    x = np.linspace(a, b, q + 1)
    y = f(x)
    return x, y

def test_discrete():
    assert(abs(discrete_func(2)[1][-1] - (1.0 / np.exp(1))) < 1e-6), 'Failure'

def S_k(a, b, xp, q):
    h = (b - a) / float(q)
    k = int((xp - a) / h) + 1
    var = discrete_func(a, b, q)
    return var[1][k] + ((var[1][k + 1] - var[1][k]) / (var[0][k + 1] - var[0][k])) * (xp - var[0][k])

def error(a, b, xp, q):
    return abs(f(xp) - S_k(a, b, xp, q))