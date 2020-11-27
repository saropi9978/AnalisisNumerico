import pylab as pylab
import math
errorI=[]
iteraciones=[]
def biseccion(f,a,b,N):
    if f(a)*f(b) >= 0:
        print("Imposible de hacer por aca")
        return None
    a_n = a
    b_n = b
    for n in range(1,N+1):
        errorI.append((a_n + b_n)/2)
        iteraciones.append(n)
        m_n = (a_n + b_n)/2
        f_m_n = f(m_n)
        if f(a_n)*f_m_n < 0:
            a_n = a_n
            b_n = m_n
        elif f(b_n)*f_m_n < 0:
            a_n = m_n
            b_n = b_n
        elif f_m_n == 0:
            print("La encontre")
            return m_n
        else:
            print("Paila, no esta la raiz en el intervalo")
            return None
    return (a_n + b_n)/2




f1= lambda x: (math.cos(2*x)**2) - x**2
f2= lambda x: (x*math.sin(x)) - 1
f3 = lambda x: ((x**3) - (2*(x)**2) + ((4/3)*x) - (8/27) )
f4 = lambda x: (9*math.sin(x))-(8*math.sin(2*x))-(3*math.sin(3*x))-4
f5 = lambda x: math.cos(1/x)

approx_phi = biseccion(f5,0.1,0.9,100)
print(approx_phi)
print("numero de iteraciones:", iteraciones[len(iteraciones)-1])

# pylab.title("Iteraciones vs Error Caso dos.")
# #pylab.plot(nIteraciones,errorI)
# pylab.xlabel('(x) iteraciones ')
# pylab.ylabel('(y) error')
# #pylab.plot(nIteraciones,errorI, color="blue", linewidth=2.5, linestyle="-", label="Punto fijo")
# pylab.plot(iteraciones, errorI, color="red",  linewidth=2.5, linestyle="-", label="Biseccion") 
# pylab.legend(loc='upper right')
# pylab.show()