from testFunctions import fTest, fEkli, fSphere, fRosen, fBila, fGoldmanPrise, fButa, fBukina, fMatyas, fLevi, fVerblud, fIzoma, fMakKormika, fShaffera2, fShaffera4
from gradientDescent import gradientDescent
from printResults import printResults
from plotGraph import plot2D
from scipy.optimize import minimize

x0 = [4, 4]
l = 0.2
a, b = -10, 10

f = fTest
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

x1_history, y1_history, a1_history, i1_counter, t1 = gradientDescent(f, x0=x0, regularized=False)
x2_history, y2_history, a2_history, i2_counter, t2 = gradientDescent(f, x0=x0, l = l, regularized=True)

printResults(x1_history, y1_history, x2_history, y2_history, i1_counter, i2_counter, l, f, t1, t2)
plot2D(a=a, b=b, x1_history=x1_history, y1_history=y1_history, x2_history=x2_history, y2_history=y2_history, function=f)
