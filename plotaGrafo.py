#!/usr/bin/env python
# coding: utf-8
#importando a biblioteca igraph
from igraph import *
import math
import random



#sorteando valores de 0 a 100 para uma lista tamanho n
def sorteio(lista,n):
        for i in range (0 , n):
                lista.append(math.ceil(100*random.random()))
        return lista

#cálculo da distancia de dois pontos:
def distancia (P1x,P1y,P2x,P2y):
        Px = (P1x - P2x)**2
        Py = (P1y - P2y)**2
        d = Px + Py
        d = d**(1/2.0)
        return d


#cálculo da força de repulsão:
def Frep (P1x,P1y,P2x,P2y):
        d = distancia (P1x,P1y,P2x,P2y)
        f = 1/(d**(1/2.0))
        return f

#cálculo da força de atração:
def Fat (P1x,P1y,P2x,P2y):
        import math
        d = distancia (P1x,P1y,P2x,P2y)
        f = 2*(math.log10(d))
        return f


# class f(object):
#     def calcule():
#         raise NotImplementedError("sfjshdjkfsdfhsjdfhsjhfjshjsd")
#         

#as funções a seguir não estão prontas:
#Fatx
def Fatx(P1x,P1y,P2x,P2y):
        f = Fat(P1x,P1y,P2x,P2y)
        d = distancia(P1x,P1y,P2x,P2y)
        x = P1x - P2x
        if (x<0):
                x = x*(-1)
        return f*(x/d)

#Faty
def Faty(P1x, P1y, P2x, P2y):
        f = Fat(P1x, P1y, P2x, P2y)
        d = distancia(P1x,P1y,P2x,P2y)
        y = P1y - P2y
        if (y<0):
                y = y*(-1)
        return f*(y/d)


#Frepx
def Frepx(P1x,P1y,P2x,P2y):
        f = Fat(P1x,P1y,P2x,P2y)
        d = distancia(P1x,P1y,P2x,P2y)
        x = P1x - P2x
        if (x<0):
                x = x*(-1)
        return f*(x/d)

#Frepy
def Frepy(P1x,P1y,P2x,P2y):
        f = Fat(P1x,P1y,P2x,P2y)
        d = distancia(P1x,P1y,P2x,P2y)
        y = P1y - P2y
        if (y<0):
                y = y*(-1)
        return f*(y/d)


#cálculo da Resultante das Forças de um ponto em X:
def Rfx(g,Pu, vizinhos,n_vizinhos):
        Rfx = 0
        # pegando a coordenada X do Vértice u que está na posição Pu
        Ux = g.vs["x"][Pu]
        # pegando a coordenada Y do Vértice u que está na posição Pu
        Uy = g.vs["y"][Pu]

        for i in range (0, len(vizinhos)):
        # for vizinho in vizinhos:
                #pegando as coordenadas dos vizinhos
                #pegando a coordenada X do Vértice V:
                j = vizinhos[i]
                Vx = g.vs["x"][j]
                # valor_x = grafico.vertices["x"][vizinho]
                #pegando a coordenada Y do Vértice V:
                Vy = g.vs["y"][j]
                fx = Fatx(Ux,Uy,Vx,Vy)
                Rfx = Rfx + fx
        for i in range (0 , len(n_vizinhos)):
                #pegando as coordenadas dos não vizinhos
                #pegando a coordenada X do Vértice V:
                j = n_vizinhos[i]
                Vx = g.vs["x"][j]
                #pegando a coordenada Y do Vértice V:
                Vy = g.vs["y"][j]
                fx = Frepx(Ux,Uy,Vx,Vy)
                # forca_x = calcula_forca_repulsao(1,2,3,4)
                Rfx = Rfx - fx
        return Rfx



#cálculo da Resultante das Forças de um ponto em Y:
def Rfy(g,Pu, vizinhos,n_vizinhos):
        Rfy = 0
        #pegando a coordenada X do Vértice u que está na posição Pu
        Ux = g.vs["x"][Pu]
        #pegando a coordenada Y do Vértice u que está na posição Pu
        Uy = g.vs["y"][Pu]
        for i in range (0 , len(vizinhos)):
                #pegando as coordenadas dos vizinhos
                #pegando a coordenada X do Vértice V:
                j = vizinhos[i]
                Vx = g.vs["x"][j]
                #pegando a coordenada Y do Vértice V:
                Vy = g.vs["y"][j]
                fy = Faty(Ux,Uy,Vx,Vy)
                Rfy = Rfy + fy
        for i in range (0 , len(n_vizinhos)):
                #pegando as coordenadas dos não vizinhos
                #pegando a coordenada X do Vértice V:
                j = n_vizinhos[i]
                Vx = g.vs["x"][j]
                #pegando a coordenada Y do Vértice V:
                Vy = g.vs["y"][j]
                fy = Frepy(Ux,Uy,Vx,Vy)
                Rfy = Rfy - fy
        return Rfy




#cálculo da nova posição da coordenada x:
def Pos_x(x,Fr):
        return x + (0.1*Fr)



#cálculo da nova posição da coordenada y:
def Pos_y(y,Fr):
        return y + (0.1*Fr)



#abrindo arquivo
f = open('grafo2.txt','r')
t = f.readlines()




#iniciando conjunto de arestas E e vértices V

V = []
E = []
matriz = []
xCoord=[]
yCoord=[]



#iniciando variável matriz
for l in t:
        matriz.append(l.split())



#preenchendo conjunto de vértices V
k = len(matriz) - 1

for i in range (0 , k):
        V.append(matriz[0][i])



#criando Grafo G
G = Graph()







#Adicionando vértices ao Grafo
G.add_vertices(len(V))

#Lista de id dos Vertices
idVertices = []
for i in range(0 , len(V) ):
        idVertices.append(i)


#Adicionando arestas ao grafo G
for i in range(1 , k +1 ):
        for j in range (1 , k + 1):
                #Caso valor da matriz seja 1, é adicionada a aresta

                print "adicionando aresta(",i-1,",",j-1,")"#preenchendo as arestas ao Grafo
                print "matriz:",matriz[i][j]
                if matriz[i][j] == "1":
                        print "inserir"
                        G.add_edges([(i-1,j-1)])

                else:
                        print "não insere"


#Adicionando as arestas ao conjunto E:
E = G.get_edgelist()


#Iniciando a Lista de Fatt com valores 0
Fatt = []
for i in range(0 , len(E) ):
        Fatt.append(0)

G.es["Fatt"] = Fatt


#Iniciando a Lista de Frep com valores 0
Frep = []
for i in range(0 , len(E) ):
        Frep.append(0)

G.es["Frep"] = Frep



#Gerando coordenadas aleatórias
xCoord = sorteio(xCoord, len(V))
yCoord = sorteio(yCoord, len(V))

#passando as coordenadas para o Grafo G
G.vs['x']=xCoord
G.vs['y']=yCoord


#labels dos vértices
G.vs["nome"] = V
G.vs["label"] = G.vs["nome"]

#layout = g.layout("kk")



#arquivo para as forças:
arq = open('forcas/Fresultante.txt', 'w')
texto = []
texto.append("Coordenadas iniciais de X: "+str(G.vs['x'])+"\n")
texto.append("Coordenada iniciais de Y: "+str(G.vs['y'])+"\n")


#plot(G)

#plot(G,  bbox = (500, 500), margin = 100)



#--------------------
#Algoritmo Spring embedding:
        #1- posicionar os vértices em locais aleatórios
        #2- Para cada vértice u, calcular as forças resultantes nas direções x e y
        #3- reposicionar o vértice
        #4- retornar ao passo 2 para M iterações
#--------------------

#Eades P. A Heuristic for Graph Drawing Congressus Numerantium
#Lei de Hooke F = K.x
#Lei de Coulomb F = K |Q1||Q2|/d


#--------------------





for M in range(100 ):
        texto.append("Loop "+str(M)+"\n")
        texto.append('---\n')
        xNovo = []
        yNovo = []
        n_vizinhos= []
        v = []
        #Loop para todos os vértices
        for i in range(0, len(V)):
                #achando os não vizinhos
                n_vizinhos = list(set(idVertices) - set(G.neighbors(i)))
                #tirando o atual da lista
                v.append(idVertices[i])
                n_vizinhos = list(set(n_vizinhos) - set(v))
                #Cálculo da força resultante:
                Fx = Rfx(G,i,G.neighbors(i),n_vizinhos)
                Fy = Rfy(G,i, G.neighbors(i),n_vizinhos)
                texto.append("Força Resultante em X: "+str(Fx)+"\n")
                texto.append("Força Resultante em Y: "+str(Fy)+"\n")
                #Reposicionando o Vértice com as novas coordenadas
                texto.append("Coordenada X: "+str(G.vs['x'][i])+"\n")
                texto.append("Coordenada Y: "+str(G.vs['y'][i])+"\n")
                x = Pos_x(G.vs['x'][i],Fx)
                y = Pos_y(G.vs['y'][i],Fy)
                xNovo.append(x)
                yNovo.append(y)
                texto.append("Nova Coordenada X: "+str(x)+"\n")
                texto.append("Nova Coordenada Y: "+str(y)+"\n")
        G.vs['x'] = xNovo
        G.vs['y'] = yNovo
        plot (G,"grafos/Grafo"+str(M)+".png",(200,200))
        texto.append('---\n')

arq.writelines(texto)
arq.close()
f.close()
#--------------------

#página de consulta:
#http://igraph.org/python/doc/tutorial/tutorial.html


# class Vertice:
#     vertices = []
#     @classmethod
#     def _v1():
#         pass
#
#
#     def _v2():
#         pass
#
#     def calcula_vertice:
#         v1()
#         v2()
#
#
#
# V.v1()
# class G:
#     v = Vertice
#     def calcula_forca:
#         pass
#
#     @property
#     def vertices(self):
#         return self.v.vertices
#
#
#     def calcula_coodenada():
#         pass


# g = G()
# forca = g.calcula_forca()
# vertice = g.v.calcula_vertice()
# g.vertices

#Pegando os vizinhos de um vértice:
#G.neighbors(2)

#Pegando o nome de um vértice:
#G.vs["nome"][0]


#verificando se é vizinho
#if (1 in vizinhos):
#    print "é vizinho"


#Pegando as coordenadas X:
#G.vs['x']

#Pegando as coordenadas y:
#G.vs['y']

#Pegando os labels dos Vértices:
#G.vs['label']


#plot(G, layout = layout, bbox = (1000, 1000), margin = 100)

#plot(G)



#print "CRISTIANOOOOO"
#for l in t:
	#V.append(l.split())
	#import ipdb; ipdb.set_trace()

#V

#Coordenadas iniciais de X: [96.0, 13.0, 33.0]
#Coordenada iniciais de Y: [40.0, 71.0, 82.0]

#Coordenadas iniciais de X: [49.6266817506, 100.60289233, 79.552674344]
#Coordenada iniciais de Y: [61.5282424754, 53.4763627821, 53.417552014]
