#!/usr/bin/env python2

import sys
import copy

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

class GrafoBFS:
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
		self.cor = []
		self.dist = []
		self.pi = []

		# preenche os vetores com valores padrao para iniciar a busca em largura
		for x in xrange(0,qt_vertice):		
			self.cor.append("branco")
		for x in xrange(0,qt_vertice):
			self.dist.append(999999999)
		for x in xrange(0,qt_vertice):
			self.pi.append(-1)

def DFS(adj):
	global cycle
	cycle = []
	cor = []
	for x in range(len(adj)):		
		cor.append("branco")
	pi = []
	for x in range(len(adj)):
		pi.append(-1)
	flag = False
	for v in range(len(adj)):
		if cor[v] == "branco" and len(adj[v]) > 0:
			DFS_VISIT(adj, v, flag, cor, pi)

def DFS_VISIT(adj, u, flag, cor, pi):
	cor[u] = "cinza"
	if flag == False:
		cycle.append(u+1)
	for v in adj[u]:
		if cor[v-1] == "branco":
			pi[v-1] = u+1
			DFS_VISIT(adj, v-1, flag, cor, pi)
		if cor[v-1] == "cinza" and v != pi[u]:
			flag = True
	cor[u] = "preto"

def grafo_menos_ciclo(G):
	G1 = G
	for i in cycle:
		for j in cycle:
			if i in G1.adj[j-1]:
				G1.adj[j-1].remove(i)
	return G1

def hierholzer(adj):
	new_cycle = []
	DFS(adj)
	print cycle
	new_cycle += cycle
	adj1 = copy.deepcopy(adj)
	
	#remove cycle do grafo
	for i in cycle:
		for j in cycle:
			if i in adj1[j-1]:
				adj1[j-1].remove(i)

	for v in adj1:
		while v != []:
			DFS(adj1)
			print cycle
			new_cycle += cycle
			#remove cycle do grafo
			for i in cycle:
				for j in cycle:
					if i in adj1[j-1]:
						adj1[j-1].remove(i)
	return new_cycle


if __name__ == "__main__":
	ma, qt_vertice, qt_aresta, v_origem, v_destino, qt_pessoas = ler_arquivo()
	g = GrafoBFS(ma, qt_vertice, qt_aresta, v_origem, v_destino, qt_pessoas)
	print g.adj
	DFS(g.adj)
	#print hierholzer(g.adj)