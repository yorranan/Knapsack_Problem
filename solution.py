import random

def gerarPopulacao(tamanho):
    populacao = []
    FITNESS_ZERADO = 0
    index = 0
    for i in range(tamanho):
        populacao.append((index, preencherCromossomo(), FITNESS_ZERADO))
        index += 1

    return populacao

def preencherCromossomo():
   cromossomo = []
   i = 0
   while i < 11:
        if i < 4:
            n = 2
        elif i < 8:
            n = 4
        else:
            n = 64
        cromossomo.append(random.randrange(0, n))
        i += 1
       
   return cromossomo

def avaliarPopulacao(populacao, pesoMaximo):
    resultados = []
    for individuo in populacao:
        peso = calcularPeso(individuo[1])
        if peso <= pesoMaximo:
            fitness = pesoMaximo - peso
            resultados.append((individuo[0], individuo[1], fitness))
    return resultados

def calcularPeso(cromossomo):
    peso = 0
    lista_de_pesos = [2500, 2245, 1500, 1340, 660, 640, 620, 390, 48, 25, 18, 3]
    for i,j in zip(cromossomo, lista_de_pesos):
        peso += i*j;
    return peso
    

geracao = 0
TAM_POPULACAO = 10
PESO_MAXIMO = 15000
populacao = gerarPopulacao(TAM_POPULACAO)
nova_populacao = avaliarPopulacao(populacao, PESO_MAXIMO)
for individuo in populacao:
    print(individuo)
print("Pos avaliar:")
for individuo in nova_populacao:
    print(individuo) 
""" while geracao < 20:
    resultados = avaliarPopulacao(populacao, PESO_MAXIMO)
    geracao += 1
    print("Geração: ", geracao) """
    