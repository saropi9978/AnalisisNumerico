import pylab as pylab

eje_x=[]
eje_y=[]
for n in range(1,10000):
    cantidad_sumas=n*n
    eje_x.append(n)
    eje_y.append(cantidad_sumas)
pylab.title("orden de convergencia")
pylab.plot(eje_x,eje_y)
pylab.xlabel('(x) tamaño de la matriz "n"')
pylab.ylabel('(y) cantidad de operaciones') 
pylab.show()




# for n in range(1,1000):

#     matriz = [[1 for i in range(n)] for j in range(n)]
#     total=0
#     cantidad_sumas=-1
#     for i in matriz:
#         total+=sum(i)
#         cantidad_sumas+=n+1
#     eje_x.append(n)
#     eje_y.append(cantidad_sumas)
#     print(n, cantidad_sumas)
    

# pylab.title("orden de convergencia")
# pylab.plot(eje_x,eje_y)
# pylab.xlabel('(x) tamaño de la matriz "n"')
# pylab.ylabel('(y) cantidad de operaciones') 
# pylab.show()