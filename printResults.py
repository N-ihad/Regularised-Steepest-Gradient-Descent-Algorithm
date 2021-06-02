
def printResults(x1_history, y1_history, x2_history, y2_history, i1_counter, i2_counter, l, f, t1, t2):
    print("***** Classical gradient descent *****", )
    print("f(minX, minY)=f(", x1_history[-1], y1_history[-1], ")=", f([x1_history[-1], y1_history[-1]]))
    print("Iterations:", i1_counter)
    print("Time:", t1)
    print()

    print("***** Regularized gradient descent *****", )
    print("f(minX, minY)=f(", x2_history[-1], y2_history[-1], ")=", f([x2_history[-1], y2_history[-1]]))
    print("Iterations:", i2_counter)
    print("Lambda:", l)
    print("Time:", t2)
    print()

def printResultClassicalGradient(x1_history, y1_history, i1_counter, f, t1):
    print("***** Classical gradient descent *****", )
    print("f(minX, minY)=f(", x1_history[-1], y1_history[-1], ")=", f([x1_history[-1], y1_history[-1]]))
    print("Iterations:", i1_counter)
    print("Time:", t1)
    print()

def printResultRegularizedGradient(x2_history, y2_history, i2_counter, l, f, t2):
    print("***** Regularized gradient descent *****", )
    print("f(minX, minY)=f(", x2_history[-1], y2_history[-1], ")=", f([x2_history[-1], y2_history[-1]]))
    print("Iterations:", i2_counter)
    print("Lambda:", l)
    print("Time:", t2)
    print()

def printAveragedTime(t1, t2):
    print("***** Classical gradient descent averaged time *****", )
    print("Averaged time:", t1)
    print()

    print("***** Regularized gradient descent averaged time *****", )
    print("Averaged time:", t2)
    print()

def printClassicalGradientAveragedTime(t):
    print("***** Classical gradient descent averaged time *****", )
    print("Averaged time:", t)
    print()

def printRegularizedGradientAveragedTime(t):
    print("***** Regularized gradient descent averaged time *****", )
    print("Averaged time:", t)
    print()