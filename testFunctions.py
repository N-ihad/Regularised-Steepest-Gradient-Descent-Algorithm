import numpy as np

def fTest(x):
    return 3 * x[0] * x[0] + x[1] * x[1]

def fButa(x):
    return np.power((x[0] + 2*x[1]-7), 2.0) + np.power((2*x[0]+x[1]-5), 2.0)

def fEkli(x):
    return -20 * np.exp(-0.2 * np.sqrt(0.5*(x[0]*x[0]+x[1]*x[1]))) - np.exp(0.5 * (np.cos(2*np.pi*x[0] + np.cos(2*np.pi*x[1])))) + np.e + 20

def fSphere(x):
    return x[0]*x[0] + x[1] * x[1]

def fRosen(x):
    return 100*np.power((x[1]-x[0]*x[0]), 2) + np.power((x[0]-1), 2)

def fBila(x):
    return np.power(1.5 - x[0] + x[0]*x[1], 2) + np.power(2.25 - x[0] + x[0]*x[1]*x[1], 2) + np.power(2.625 - x[0] + x[0]*x[1]*x[1]*x[1], 2)

def fGoldmanPrise(x):
    return (1 + np.power((x[0] + x[1] + 1), 2)*(19 - 14*x[0] + 3*x[0]*x[0] - 14*x[1] + 6*x[0]*x[1] + 3*x[1]*x[1])) * (30 + (2*x[0]-3*x[1])*(2*x[0]-3*x[1])*(18 - 32*x[0] + 12*x[0]*x[0]+ 48*x[1]-36*x[0]*x[1]+27*x[1]*x[1]))

def fBukina(x):
    return 100 * np.sqrt(abs(x[1]-0.01*x[0]*x[0])) + 0.01 * abs(x[0]+10)

def fMatyas(x):
    return 0.26 * (x[0]*x[0] + x[1]*x[1]) - 0.48*x[0]*x[1]

def fLevi(x):
    return np.power(np.sin(3*np.pi*x[0]), 2) + (x[0]-1)*(x[0]-1) * (1 + np.power(np.sin(3*np.pi*x[1]), 2)) + (x[1]-1)*(x[1]-1)*(1 + np.power(np.sin(2*np.pi*x[1]), 2))

def fVerblud(x):
    return 2*x[0]*x[0] - 1.05*np.power(x[0], 4) + (np.power(x[0], 6)/6) + x[0]*x[1] + x[1]*x[1]

def fIzoma(x):
    return -np.cos(x[0])*np.cos(x[1])*np.exp(-((x[0]-np.pi)*(x[0]-np.pi)+(x[1]-np.pi)*(x[1]-np.pi)))

def fMakKormika(x):
    return np.sin(x[0] + x[1]) + (x[0]-x[1])*(x[0]-x[1]) - 1.5*x[0] + 2.5*x[1] + 1

def fShaffera2(x):
    return 0.5 + (np.power(np.cos(np.sin(abs(x[0]*x[0] - x[1]*x[1]))), 2) - 0.5) / (np.power(1+0.001*(x[0]*x[0] + x[1]*x[1]), 2))

def fShaffera4(x):
    return 0.5 + (np.power(np.sin(x[0]*x[0] - x[1]*x[1]), 2) - 0.5) / (np.power(1+0.001*(x[0]*x[0] + x[1]*x[1]), 2))