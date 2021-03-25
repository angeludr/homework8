import numpy as np
from scipy.optimize import minimize
import matplotlib.pyplot as plt

def func(x, y):
    inner1 = -((x - 1)**2) - (2 * ((y - 3)**2))
    inner2 = -2 * ((x - 4)**2) - ((y - 1)**2)
    t1 = 5 * np.exp(inner1)
    t2 = 3 * np.exp(inner2)
    return t1 + t2
    
def gradient(func = None, deriv = None, startPt = None, gamma =  None, maxiter = 1000):
    guess = startPt
    for i in range(maxiter):
        guess = guess - gamma * deriv(guess)
        print(guess)
    return guess
    
def xpartial(x, y):
    inner1 = -((x - 1)**2) - (2 * ((y - 3)**2))
    inner2 = -2 * ((x- 4)**4) - ((y - 1)**2)
    t1 = -10 * (x - 1) * np.exp(inner1)
    t2 = 12 * (x - 4) * np.exp(inner2)
    return t1 - t2

def ypartial(x, y):
    inner1 = -((y - 1)**2) - (2 * ((x - 4)**2))
    inner2 = -2 * ((y - 3)**2) - ((x - 1)**2)
    t1 = -6 * (y - 1) * np.exp(inner1)
    t2 = 20 * (y - 3) * np.exp(inner2)
    return t1 - t2


if __name__ == "__main__":

    xs = np.arange(0, 6, 0.01)
    ys = np.arange(0, 6, 0.01)
    xs, ys = np.meshgrid(xs, ys)
    
    grad = func(xs, ys)
    
    # Plotting contour plot
    # Divide axes by 100 to get the appropriate range of 0 - 5
    plt.contourf(grad)
    plt.show()
