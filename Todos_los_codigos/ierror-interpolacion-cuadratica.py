import math
import numpy
import pylab as pl
def f(x): return math.sin(x)

def p(x): return math.sin(0)+(((math.sin(0.01)-math.sin(0))/(0.01-0))*(x-0)) + (((math.sin(0.02)-math.sin(0.01))/(0.02-0.01))*(x-0)*(x-0.01))

def errorAbsoluto(x):
    #print("Error absoluto{:.20f}".format(abs(f(0.02)-p(0.02))))
    return abs(f(0.02)-p(0.02))

def errorGeneral(x):
    #print ("error General",(1*(x)**3)/(9*math.sqrt(3)))
    return (1*(x)**3)/(9*math.sqrt(3))


errorAbsoluto(0.01)
errorGeneral(0.01)

arreglo= []
valoresG=[]
valoresAbs= []
for i in numpy.arange(0,0.02,0.005):
    arreglo.append(i)
    valoresAbs.append(errorAbsoluto(i))
    valoresG.append(errorGeneral(i))
#end for
print("Arreglo: ", arreglo)
print("Error General: ",valoresG)
print("Errores absolutos:",valoresAbs)
#pl.title("Comparacion Error absoluto error general")
#pl.plot(arreglo, valoresAbs, color="blue", linewidth=2.5, linestyle="-", label="Error Absoluto")
pl.plot(arreglo,valoresG, color="red",  linewidth=2.5, linestyle="-", label="Error General")
pl.legend(loc='upper left')
#pl.axis([0,0.016,0,2.17e-07])
pl.show()


