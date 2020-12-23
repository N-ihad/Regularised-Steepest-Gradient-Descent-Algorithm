import numpy as np
from scipy.optimize import minimize
import numdifftools as nd
import time

np.set_printoptions(suppress=True)

def xa(a, x0, gr):
    return x0[0] - a * gr[0]

def ya(a, x0, gr):
    return x0[1] - a * gr[1]

def f(a, x0, gr, function):
    return function([xa(a, x0, gr), ya(a, x0, gr)])

def fr(a, x0, gr, function, l):
    return f(a, x0, gr, function) + a * a * l * np.inner(gr, gr)


def gradientDescent(function, x0=[0, 0], l = 1, regularized = False):
    startTime = time.time()
    x_history = []
    y_history = []
    a_history = []
    i_counter = 1
    x_k = x0
    x_history.append(x_k[0])
    y_history.append(x_k[1])
    gr = nd.Gradient(function)([x_k])
    a = minimize(fr, 0, args=(x_k, gr, function, l), method='Nelder-Mead', tol=1e-6).x if regularized else minimize(f, 0, args=(x_k, gr, function), method='Nelder-Mead', tol=1e-6).x
    a_history.append(a)

    while True:
        x_k = [xa(a, x_k, gr), ya(a, x_k, gr)]
        x_history.append(x_k[0])
        y_history.append(x_k[1])
        gr = nd.Gradient(function)([x_k])
        a = minimize(fr, 0, args=(x_k, gr, function, l), method='Nelder-Mead', tol=1e-6).x if regularized else minimize(f, 0, args=(x_k, gr, function), method='Nelder-Mead', tol=1e-6).x
        a_history.append(a)
        i_counter += 1
        if np.linalg.norm(gr) < 1e-5:
            break
    endTime = time.time()
    timeElapsed = endTime - startTime
    return x_history, y_history, a_history, i_counter, timeElapsed