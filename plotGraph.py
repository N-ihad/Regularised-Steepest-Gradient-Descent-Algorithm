from pylab import meshgrid,cm,imshow,contour,clabel,colorbar,axis,title,show
import matplotlib.pyplot as plt
import numpy as np

def plot2D(a, b, x1_history, y1_history, x2_history, y2_history, function):
    markersize = 2
    x = np.linspace(a, b, 50)
    y = np.linspace(a, b, 50)
    X, Y = np.meshgrid(x, y)
    Z = function([X, Y])
    plt.subplots(1, 2, figsize=(12, 6))
    plt.subplot(1, 2, 1)
    plt.title = "something"
    plt.contourf(X, Y, Z, 20, cmap='RdGy')
    plt.colorbar()
    plt.plot(x1_history, y1_history)
    plt.plot(x1_history, y1_history, 'wo', markersize=markersize)

    plt.subplot(1, 2, 2)
    plt.contourf(X, Y, Z, 20, cmap='RdGy')
    plt.colorbar()
    plt.plot(x2_history, y2_history)
    plt.plot(x2_history, y2_history, 'wo', markersize=markersize)

    plt.tight_layout()
    plt.show()

def plot3D(a, b, function):
    fig = plt.figure()
    ax = fig.gca(projection='3d')
    X = np.arange(a, b, 0.25)
    Y = np.arange(a, b, 0.25)
    X, Y = np.meshgrid(X, Y)
    Z = function([X, Y])
    ax.plot_surface(X, Y, Z, cmap="RdGy", linewidth=0, antialiased=False)

    plt.show()

