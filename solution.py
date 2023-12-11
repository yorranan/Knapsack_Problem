import random

def gerarPopulacao(tamanho):
    populacao = []
    index = 0
    for i in range(tamanho):
        populacao.append((index, preencherCromossomo()))
        index += 1

    return populacao

def preencherCromossomo():
   cromossomo = []
   n = 2
   while n <= 4096:
       cromossomo.append(random.randrange(0, n))
       n *= 2
   return cromossomo
    

geracao = 0
TAM_POPULACAO = 10
PESO_MAXIMO = 7000
populacao = gerarPopulacao(TAM_POPULACAO)
""" while geracao < 20:
    resultados = avaliarPopulacao(populacao, PESO_MAXIMO)
    geracao += 1
    print("Geração: ", geracao) """
    