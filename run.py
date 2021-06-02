from testFunctions import fLeviMontavlo, fNeumaier, fSalomon, fTest, fSchwefel, fShubert, fGriewank, fEkli, fSphere, fRosen, fBila, fGoldmanPrise, fButa, fBukina, fMatyas, fLevi, fVerblud, fIzoma, fMakKormika, fShaffera2, fShaffera4
from gradientDescent import gradientDescent
from printResults import printResults, printAveragedTime, printResultClassicalGradient, printResultRegularizedGradient, printClassicalGradientAveragedTime, printRegularizedGradientAveragedTime
from plotGraph import plot2D, plot3D
from scipy.optimize import minimize
from statistics import mean

# f = fTest
f = fLeviMontavlo
# f = fNeumaier
# f = fSalomon
# f = fSchwefel
# f = fShubert
# f = fGriewank
# f = fEkli
# f = fSphere
# f = fRosen
# f = fBila
# f = fGoldmanPrise
# f = fButa
# f = fBukina
# f = fMatyas
# f = fLevi
# f = fVerblud
# f = fIzoma
# f = fMakKormika
# f = fShaffera2
# f = fShaffera4

x0 = [4, 4]
l = 1
a, b = -10, 10
times = []

for _ in range(20):
    x1_history, y1_history, a1_history, i1_counter, t1 = gradientDescent(f, x0=x0, regularized=False)
    # printResultClassicalGradient(x1_history, y1_history, i1_counter, f, t1)
    times.append(t1)
printClassicalGradientAveragedTime(round(mean(times), 3))
# t1 = mean(times)

times = []
for _ in range(20):
    x2_history, y2_history, a2_history, i2_counter, t2 = gradientDescent(f, x0=x0, l = l, regularized=True)
    # printResultRegularizedGradient(x2_history, y2_history, i2_counter, l, f, t2)
    times.append(t1)
printRegularizedGradientAveragedTime(round(mean(times), 3))
# t2 = mean(times)

printResults(x1_history, y1_history, x2_history, y2_history, i1_counter, i2_counter, l, f, "---", "---")
# plot2D(a=a, b=b, x1_history=x1_history, y1_history=y1_history, x2_history=x2_history, y2_history=y2_history, function=f)
# plot3D(a, b, f)