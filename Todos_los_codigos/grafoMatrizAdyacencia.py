import numpy
class GrafoMatrizAdyacencia():
    def __init__(self):
        self.matriz=[]
    
    def imprimir(self):
        for i in self.matriz:
            for j in i:
                print(j,end=" ")
            print()
        print()
    
    def agregarArista(self, v1,v2):
        tam=max(v1.id,v2.id)
        if len(self.matriz)<tam:
            
            for i in range(len(self.matriz)):
                for j in range(len(self.matriz),tam):
                    self.matriz[i].append(None)
            for i in range(len(self.matriz),tam):    
                self.matriz.append([None]*tam)
        self.matriz[v1.id-1][v2.id-1]=1

    def vecinos(self, v,vertices):
        lista=[]
        for i in range(len(self.matriz)):
            if not self.matriz[v.id-1][i] is None:
                lista.append(vertices[self.matriz[v.id-1][i]])
        return lista
                
    def explorar(self, v):#vertice
        pass
            
    def dfs(self):
        pass


class Vertice():
    def __init__(self, id, contenido, marca=0):
        self.id=id
        self.contenido=contenido
        self.marca=marca    
    def getId(self):
        return self.id
    def getContenido(self):
        return self.contenido
    def getMarca(self):
        return self.marca

v1=Vertice(1,"hola")
v2=Vertice(2,"hola")
v3=Vertice(3,"hola")
v5=Vertice(5,"hola")
vertices={
    1:v1,
    2:v2,
    3:v3,
    5:v5
}
grafo= GrafoMatrizAdyacencia()
grafo.agregarArista(v1,v2)
grafo.agregarArista(v5,v3)
print(vertices[1].getId())




