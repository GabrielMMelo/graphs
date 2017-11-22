#!/usr/bin/python3

import sys

def ler_arquivo():
    nome_arquivo = sys.argv[1]
    # Armazena quantidade de vertices e aresta e armazena o
    # conteudo do arquivo em uma matriz de adjacencia
    arquivo = open(nome_arquivo, 'r')

    temp = arquivo.readline().split()
    qt_vertice = int(temp[0])
    qt_aresta = int(temp[1])

    # Inicializa a matriz = 0
    ma = [[0 for i in range(qt_vertice)] for j in range(qt_vertice)]

    temp = 0
    for linha in arquivo:
        temp = temp + 1
        valores = linha.split()
        if int(valores[0]) != 0 and int(valores[1]) != 0 and temp <= qt_aresta:
            ma[ int(valores[0])-1 ][ int(valores[1])-1 ] = int(valores[2])
            ma[ int(valores[1])-1 ][ int(valores[0])-1 ] = int(valores[2])

    arquivo.close()

    # Armazena o vertice de origem e destino, e a quantidade
    # de pessoas
    arquivo = open(nome_arquivo, 'r')

    lista_linhas = arquivo.readlines()
    qt_linhas = len(lista_linhas)
    temp = lista_linhas[qt_linhas-2].split()

    v_origem = int(temp[0])
    v_destino = int(temp[1])
    qt_pessoas = int(temp[2])

    arquivo.close()

    return ma, qt_vertice, qt_aresta, v_origem, v_destino, qt_pessoas
    

class Grafo:
    def __init__(self, ma, qt_vertice, qt_aresta, v_origem, v_destino, qt_pessoas):
        self.ma = ma
        self.adj = [[] for i in range(0,qt_vertice)]

        # cria lista de adjacencias
        for i in xrange(0,qt_vertice):          
            for j in xrange(0,qt_vertice):
                if self.ma[i][j]!=0:
                    self.adj[i].append(j+1)

        self.qt_vertice = qt_vertice
        self.qt_aresta = qt_aresta
        self.v_origem = v_origem
        self.v_destino = v_destino
        self.qt_pessoas = qt_pessoas
        self.flag = []
        self.dist = []
        #self.distVolta = []
        self.pi = []

        # preenche os vetores com valores padrao para iniciar a busca em largura
        for x in xrange(0,qt_vertice):      
            self.flag.append(True)
        for x in xrange(0,qt_vertice):
            self.dist.append(-1)
        #for x in xrange(0,qt_vertice):
        #    self.distVolta.append(-1)
        for x in xrange(0,qt_vertice):
            self.pi.append(-1)

def Dijkstra(G,origem):
	G.dist[origem-1] = 0
	while (G.flag[G.v_destino-1] != False):

        #Seleciona o vetor de menor distancia
		maior = -1
		indice = 0
		indice_maior = 0
		for v in G.dist:
			if v > maior and G.flag[indice]:
				maior = v
				indice_maior = indice
			indice = indice + 1
		u = indice_maior

		G.flag[u] = False

		for v in G.adj[u]:
			
			if u == origem - 1:
    				G.dist[v-1] =  G.ma[u][v-1]
    				G.pi[v-1] = u+1

			else:
				if (G.flag[v-1]) and (G.ma[u][v-1] > G.dist[u]):
					if(G.dist[v-1] < G.dist[u]):
						G.dist[v-1] =  G.dist[u]
						G.pi[v-1] = u+1
				elif (G.flag[v-1]) and (G.ma[u][v-1] < G.dist[u]):
					if G.dist[v-1] < G.ma[u][v-1]:
						G.dist[v-1] = G.ma[u][v-1]
						G.pi[v-1] = u+1
	print(G.qt_pessoas)
	total = G.qt_pessoas
	contador = 0
	while total > 0:
		total = total - (G.dist[v_destino-1]-1)
		contador = contador + 1
	print ("Viagens: " + str(contador))
	print G.dist
	print G.pi

if __name__ == "__main__":
    ma, qt_vertice, qt_aresta, v_origem, v_destino, qt_pessoas = ler_arquivo()
    g = Grafo(ma, qt_vertice, qt_aresta, v_origem, v_destino, qt_pessoas)
    Dijkstra(g,g.v_origem)