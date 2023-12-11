import random

def gerarPopulacao(tamanho):
    populacao = []
    for i in range(tamanho):
        populacao.append(preencherCromossomo())
    
    return populacao

import random

def gerarPopulacao(tamanho):
    populacao = []
    index = 0
    for i in range(tamanho):
        populacao.append((index, preencherCromossomo()))
        index += 1

    return populacao

def preencherCromossomo():
   TAM = 12
   cromossomo = [None]*TAM
   n = 2
   index = 0
   while n <= 4096:
       cromossomo = random.randrange(0, n)
       n *= 2
   return cromossomo


def calcularPesoTotal(individuo, pesos):
    peso_total = 0
    for i, j in zip(individuo, pesos):
        peso_total += i[1]*j
    return peso_total

def calcularFitness(individuo, limite):
    pesos = [2500, 2245, 1500, 1340, 660, 
             640, 620, 390, 47.54, 25.4, 19.8, 3.2]
    fitness = abs(limite-calcularPesoTotal(individuo, pesos))
    return fitness

def avaliarPopulacao(populacao, limite):
    resultados = []
    for index, individuo in enumerate(populacao):
        resultados.append((calcularFitness(individuo, limite), index))
    return resultados



geracao = 0
TAM_POPULACAO = 10
PESO_MAXIMO = 7000
populacao = gerarPopulacao(TAM_POPULACAO)
print(avaliarPopulacao(populacao, PESO_MAXIMO))
""" while geracao < 20:
    resultados = avaliarPopulacao(populacao, PESO_MAXIMO)
    geracao += 1
    print("Geração: ", geracao) """
    

def calcularPesoTotal(individuo, pesos):
    peso_total = 0
    for i, j in zip(individuo, pesos):
        peso_total += i[1]*j
    return peso_total

def calcularFitness(individuo, limite):
    pesos = [2500, 2245, 1500, 1340, 660, 
             640, 620, 390, 47.54, 25.4, 19.8, 3.2]
    fitness = abs(limite-calcularPesoTotal(individuo, pesos))
    return fitness

def avaliarPopulacao(populacao, limite):
   resultados = []
   for index, individuo in enumerate(populacao):
       resultados.append((calcularFitness(individuo[1], limite), index))
   return resultados


geracao = 0
TAM_POPULACAO = 10
PESO_MAXIMO = 7000
populacao = gerarPopulacao(TAM_POPULACAO)
print(avaliarPopulacao(populacao, PESO_MAXIMO))
""" while geracao < 20:
    resultados = avaliarPopulacao(populacao, PESO_MAXIMO)
    geracao += 1
    print("Geração: ", geracao) """
    