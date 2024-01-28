import random
from math import inf
import time

def gerarPopulacaoInicial(tamanho):
    populacao = []
    for i in range(tamanho):
        populacao.append((geracao, preencherCromossomo(), FITNESS_ZERADO))
    return populacao

def inicializarGeracao(populacao_existente):
    populacao = []
    global geracao
    for i in populacao_existente:
        populacao.append((geracao+1, i, FITNESS_ZERADO))
    return populacao

def preencherCromossomo():
   cromossomo = []
   i = 0
   while i < TAMANHO_CROMOSSOMO-1:
        cromossomo.append(random.randrange(0, 1))
       
   return cromossomo

def avaliarPopulacao(populacao):
    resultados = []
    for individuo in populacao:
        peso, fitness = calcular(individuo[1])
        if peso <= PESO_MAXIMO:
            resultados.append((individuo[0], individuo[1], fitness))
    return resultados

def calcular(cromossomo):
    peso = 0
    valor = 0
    lista_de_valores = [20, 25, 5, 1, 1, 4, 5, 8, 9, 10]
    lista_de_pesos = [5, 10, 2, 3, 8, 4, 9, 1, 2, 6]
    for i,j in zip(cromossomo, lista_de_pesos):
        peso += i*j
    for i, j in zip(cromossomo, lista_de_valores):
        valor += i*j
    return peso, valor

def selecionarElite(populacao, tamanho):
    melhores_resultados = []
    populacao.reverse()
    i = 0
    while i < tamanho:
        try:
            melhores_resultados.append(populacao.pop())
        except IndexError:
            print('A lista está vazia')
        i += 1
    return melhores_resultados

def gerarFilhos(populacao):
    filhos = []
    tamanho = TAX_CROSSOVER
    while tamanho > 0 and len(populacao) >= 2:
        pai = populacao.pop(random.choice(range(len(populacao))))
        mae = populacao.pop(random.choice(range(len(populacao))))
        filho = pai[1][:6] + mae[1][6:]
        filha = mae[1][:6] + pai[1][6:]
        filhos.append(filha)
        filhos.append(filho)
        tamanho -= 1
    return filhos

def imprimirPopulacao(mensagem, populacao):
    print(mensagem)
    for individuo in populacao:
        print(individuo)

def completarPopulacao(populacao):
    while(TAM_POPULACAO > len(populacao)):
        aux = gerarPopulacaoInicial(TAM_POPULACAO-len(populacao))
        populacao.extend(aux)
    return populacao

def melhorResultado(populacao):
    global melhor_resultado
    global melhor_fitness
    try:
        if populacao[0][2] > melhor_fitness:
            melhor_fitness = populacao[0][2]
            melhor_resultado = populacao[0]
    except IndexError:
        print("Fora do range")
    
def mutar(populacao):
   for individuo in populacao:
       cromossomo = individuo[1]
       for i in range(len(cromossomo)):
            cromossomo[i] = random.randrange(0, 1)   
   return avaliarPopulacao(populacao)


tempo_o = time.time()
TAXA_DE_MUTACAO = float(input("Taxa de Mutacao: "))/100
TAM_POPULACAO = int(input("Tamanho da Populacao: "))
TAX_CROSSOVER = int(input("Taxa de Crossover: "))%TAM_POPULACAO
TAM_ELITE = 10%TAM_POPULACAO
TAM_MUTACAO = 5%TAM_POPULACAO
PESO_MAXIMO = 12
POSICAO_INDEX = 0
POSICAO_CROMOSSOMO = 1
POSICAO_FITNESS = 2
NUM_GERACOES = int(input("Numero de Geracoes: "))
geracao = 0
max_index = 0
nova_geracao = []
populacao = []
melhor_resultado = None
melhor_resultado_final = None
melhor_fitness = inf
#Primeira rodada:
populacao = gerarPopulacaoInicial(TAM_POPULACAO)
resultados = avaliarPopulacao(populacao)
imprimirPopulacao(resultados)
elite = selecionarElite(resultados)
imprimirPopulacao(elite)
imprimirPopulacao(resultados)
print("Melhor resultado global:")
print(melhor_resultado)
print("Resultado iteração final:")
print(nova_geracao[0])
print("Tempo de execução: {:.1f}".format(time.time()-tempo_o))

