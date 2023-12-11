import random

def gerarPopulacao(tamanho, index_max, populacao_existente):
    populacao = []
    FITNESS_ZERADO = 0
    index = index_max
    if populacao_existente != None:
        for i in populacao_existente:
            populacao.append((index, i, FITNESS_ZERADO))
            index += 1
    else:
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

def selecionaElite(populacao, tamanho):
    elite = []
    i = 0
    while i < tamanho:
        elite.append(populacao.pop())
        i += 1
    return elite

def gerarFilhos(populacao):
    filhos = []
    POSICAO_FITNESS = 2

    while len(populacao) >= 2:
        pai = populacao.pop(random.choice(range(len(populacao))))
        mae = populacao.pop(random.choice(range(len(populacao))))
        filho = pai[1][:6] + mae[1][6:]
        filha = mae[1][:6] + pai[1][6:]
        filhos.append(filha)
        filhos.append(filho)

    return filhos
    
geracao = 0
TAM_POPULACAO = 20
TAM_ELITE = 25%TAM_POPULACAO
TAM_CROSSOVER = 50%TAM_POPULACAO
TAM_MUTACAO = 25%TAM_POPULACAO
PESO_MAXIMO = 12000
max_index = 0
nova_geracao = []
populacao = gerarPopulacao(TAM_POPULACAO, max_index, None)
populacao = sorted(populacao, key=lambda x: x[0], reverse=True)
max_index = populacao[0][0]
populacao = avaliarPopulacao(populacao, PESO_MAXIMO)
populacao = sorted(populacao, key=lambda x: x[2], reverse=True)
print("populacao")
for i in populacao:
    print(i)
elite = selecionaElite(populacao, TAM_ELITE)
populacao.reverse()
para_mutacao = selecionaElite(populacao, TAM_MUTACAO)
print("mutantes:")
for i in para_mutacao:
    print(i)
nova_geracao = gerarPopulacao(None, max_index, gerarFilhos(populacao))
nova_geracao = avaliarPopulacao(nova_geracao, PESO_MAXIMO)
nova_geracao.extend(elite)
print("elite:")
for i in elite:
    print(i)
print("cross e elite:")
for i in nova_geracao:
    print(i)
nova_geracao = sorted(nova_geracao, key=lambda x: x[0], reverse=True)
max_index = nova_geracao[0][0]
while(TAM_POPULACAO > len(nova_geracao)):
    aux = gerarPopulacao(TAM_POPULACAO-len(nova_geracao), max_index, None)
    aux = avaliarPopulacao(aux, PESO_MAXIMO)
    nova_geracao.extend(aux)
print("preenchido:")
for i in nova_geracao:
    print(i)
"""
 while geracao < 20:
    resultados = avaliarPopulacao(populacao, PESO_MAXIMO)
    geracao += 1
    print("Geração: ", geracao) """
    