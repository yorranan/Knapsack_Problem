import matplotlib.pyplot as plt
import random
import csv
import time
import pandas as pd

TAMANHO_CROMOSSOMO = 16
PESO_MAXIMO = 13

def preencherPopulacao(tamanho):
    global geracao
    populacao = []
    for i in range(tamanho):
        populacao.append((geracao, preencherCromossomo(), 0))
    populacao = avaliarPopulacao(populacao)
    return populacao

def preencherCromossomo():
    cromossomo = []
    i = 0
    while i < TAMANHO_CROMOSSOMO:
        cromossomo.append(random.randrange(0, 2))
        i += 1
    while calcularPeso(cromossomo) > PESO_MAXIMO:
        cromossomo[random.randint(0, TAMANHO_CROMOSSOMO-1)] = 0
    return cromossomo

def avaliarPopulacao(populacao):
    resultados = []
    for individuo in populacao:
        fitness = calcularFitness(individuo[1])
        resultados.append((individuo[0], individuo[1], fitness))
    return resultados

def calcularFitness(cromossomo:list):
    fitness = 0
    lista_de_valores = [2, 7, 3, 4, 5, 2, 6, 10, 4, 8, 7, 12, 1, 5, 16, 2]
    for i, j in zip(cromossomo, lista_de_valores):
        fitness += i * j
    return fitness

def calcularPeso(cromossomo:list):
    peso = 0
    lista_de_pesos = [6, 3, 1, 7, 4, 2, 5, 3, 5, 1, 6, 10, 1, 2, 20, 3]
    for i, j in zip(cromossomo, lista_de_pesos):
        peso += i * j
    return peso

def selecionarElite(populacao):
    melhores_resultados = []
    populacao.sort(key=lambda x: x[2], reverse=True)
    i = 0
    while i < TAMANHO_ELITE:
        try:
            melhores_resultados.append(populacao.pop(0))
        except IndexError:
            print('A lista está vazia')
        i += 1
    return melhores_resultados

def gerarFilhos(populacao:list):
    filhos = []
    global geracao
    tax = TAX_CROSSOVER
    tam_lista = len(populacao)
    while tam_lista >= 2:
        pai = populacao.pop(random.choice(range(len(populacao))))
        mae = populacao.pop(random.choice(range(len(populacao))))
        filho = pai[1][:8] + mae[1][8:]
        filhos.append((geracao, filho, 0))
        tam_lista = len(populacao)
        tax -= 1
        if tax <= 0:
            break
    return filhos + populacao

def mutar(populacao:tuple):
    i = 0
    while i < TAX_MUTACAO:
        individuo = random.choice(populacao)
        cromossomo = individuo[1]
        for _ in range(3):
            for j in range(len(cromossomo)):
                cromossomo = list(cromossomo)
                cromossomo[j] = random.randrange(0, 2)
                cromossomo = tuple(cromossomo)

        i += 1
    return populacao

def verificarMelhorResultado(populacao):
    populacao.sort(key=lambda x: x[2], reverse=True)
    resultado = populacao[0]
    global melhor_resultado_global
    if not melhor_resultado_global or resultado[2] > melhor_resultado_global[2]:
        melhor_resultado_global = resultado

melhor_fitness = []
elapsed_times = []

def EscreverNoCSV(population, filename, elapsed_time):
    global rodada
    with open(filename, 'a', newline='') as csvfile:
        writer = csv.writer(csvfile)
        for individual in population:
            writer.writerow([rodada, individual[0], individual[1], individual[2], elapsed_time])
            melhor_fitness.append(individual[2])


with open('melhores_resultados.csv', 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(['Rodada', 'Geracao', 'Cromossomo', 'Fitness', 'Tempo de Execução'])

n = int(input("Número de casos:"))
for rodada in range(n):
    start_time = time.time()
    TAMANHO_POPULACAO = int(input("Tamanho da Populacao : "))
    TAX_CROSSOVER = int(input("Taxa de Crossover : "))//TAMANHO_POPULACAO
    TAX_MUTACAO = int(input("Taxa de Mutacao : "))//TAMANHO_POPULACAO
    NUM_GERACOES = int(input("Numero de Geracoes : "))
    TAMANHO_ELITE = 20//TAMANHO_POPULACAO
    geracao = 0
    melhor_resultado_global = None
    populacao = preencherPopulacao(TAMANHO_POPULACAO)
    elite = selecionarElite(populacao)
    filhos = gerarFilhos(populacao)
    filhos = mutar(filhos)
    populacao.clear()
    populacao = elite + filhos + preencherPopulacao(TAMANHO_POPULACAO-len(elite)-len(filhos))
    populacao = avaliarPopulacao(populacao)
    elite.clear()
    filhos.clear()

    while geracao < NUM_GERACOES:
        geracao += 1
        elite = selecionarElite(populacao)
        filhos = gerarFilhos(populacao)
        filhos = mutar(filhos)
        populacao.clear()
        populacao = elite + filhos + preencherPopulacao(TAMANHO_POPULACAO-len(elite)-len(filhos))
        populacao = avaliarPopulacao(populacao)
        verificarMelhorResultado(populacao)

    elapsed_time = time.time() - start_time
    EscreverNoCSV([melhor_resultado_global], 'melhores_resultados.csv', elapsed_time)
    EscreverNoCSV(populacao, f'populacoes_final_{rodada}.csv', elapsed_time)
    elapsed_times.append(elapsed_time)

plt.plot(melhor_fitness)
plt.title('Melhores Valores de Fitness por Rodada')
plt.xlabel('Número da Rodada')
plt.ylabel('Melhor Fitness')
plt.show()
plt.plot(elapsed_times)
plt.title('Tempo de execução por rodada')
plt.xlabel('Rodada')
plt.ylabel('Tempo de execução (segundos0)')
plt.show()
