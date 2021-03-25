import numpy as np
import matplotlib.pyplot as plt
from scipy import optimize as opt

def buckingham(A, B, C, r):
    """Returns the potential energy between atoms in a solid or gas in electron volts"""
    r = np.array(r)
    pauli = A * (np.exp(-B * r))
    vanDerWaals = -C / (r**6)
    return pauli + vanDerWaals

if __name__ == "__main__":

    angstroms = np.arange(0.5, 2.5, 0.01) # Values to be computed by the buckingham potential equation
    angstroms = list(angstroms)
    phi = buckingham(1, 1, 1, angstroms)
    
    # Plotting buckingham function
    plt.plot(angstroms, phi, color = 'blue')
    plt.ylabel('eV')
    plt.xlabel('Angstroms')
    plt.title('Buckingham Potential')
    plt.show()
    
    # Defines function for scipy minimize
    fun = lambda r: -1 * (1 * np.exp(-1 * r[0]) - (1 / r[0]**6))
    
    max = opt.minimize(fun, (0, 0))
    print('The maximum for the buckingham function is', max.fun)
