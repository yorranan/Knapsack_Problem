import random
from math import inf
import time

def gerarPopulacaoInicial(tamanho):
    populacao = []
    FITNESS_ZERADO = 0
    for i in range(tamanho):
        populacao.append((geracao, preencherCromossomo(), FITNESS_ZERADO))
        
    populacao = avaliarPopulacao(populacao)
    return populacao

def inicializarGeracao(populacao_existente):
    populacao = []
    FITNESS_ZERADO = 0
    for i in populacao_existente:
        populacao.append((geracao+1, i, FITNESS_ZERADO))
    populacao = avaliarPopulacao(populacao)
    return populacao

def preencherCromossomo():
   cromossomo = []
   TAMANHO_CROMOSSOMO = 12
   i = 0
   while i < TAMANHO_CROMOSSOMO:
        
        if i < 4:
            n = 2
        elif i < 8:
            n = 4
        else:
            n = 64
        cromossomo.append(random.randrange(0, n))
        i += 1
       
   return cromossomo

def avaliarPopulacao(populacao):
    resultados = []
    for individuo in populacao:
        peso = calcularPeso(individuo[1])
        if peso <= PESO_MAXIMO:
            fitness = PESO_MAXIMO - peso
            resultados.append((individuo[0], individuo[1], fitness))
    return resultados

def calcularPeso(cromossomo):
    peso = 0
    lista_de_pesos = [2500, 2245, 1500, 1340, 660, 640, 620, 390, 48, 25, 18, 3]
    for i,j in zip(cromossomo, lista_de_pesos):
        peso += i*j;
    return peso

def selecionarMenoresFitness(populacao, tamanho):
    menores_resultados = []
    i = 0
    while i < tamanho:
        try:
            menores_resultados.append(populacao.pop())
        except IndexError:
            print('A lista está vazia')
        i += 1
    return menores_resultados

def selecionarMaioresFitness(populacao, tamanho):
    maiores_resultados = []
    populacao.reverse()
    i = 0
    while i < tamanho:
        try:
            maiores_resultados.append(populacao.pop())
        except IndexError:
            print('A lista está vazia')
        i += 1
    return maiores_resultados

def gerarFilhos(populacao):
    filhos = []
    tamanho = TAX_CROSSOVER
    while tamanho > 0 and len(populacao) >= 2:
        pai = populacao.pop(random.choice(range(len(populacao))))
        mae = populacao.pop(random.choice(range(len(populacao))))
        filho = pai[1][:6] + mae[1][6:]
        filha = mae[1][:6] + pai    [1][6:]
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
        if populacao[0][2] < melhor_fitness:
            melhor_fitness = populacao[0][2]
            melhor_resultado = populacao[0]
    except IndexError:
        print("Fora do range")
    
def mutar(populacao):
   for individuo in populacao:
       cromossomo = individuo[1]
       for i in range(len(cromossomo)):
           for j in range(4):
               if random.random() < TAXA_DE_MUTACAO:
                if i < 4:
                    cromossomo[i] = random.randrange(0, 2)
                elif i < 8:
                    cromossomo[i] = random.randrange(0, 4)
                else:
                    cromossomo[i] = random.randrange(0, 64)
            
   return avaliarPopulacao(populacao)


tempo_o = time.time()
TAXA_DE_MUTACAO = float(input("Taxa de Mutacao: "))/100
TAM_POPULACAO = int(input("Tamanho da Populacao: "))
TAX_CROSSOVER = int(input("Taxa de Crossover: "))%TAM_POPULACAO
TAM_ELITE = 10%TAM_POPULACAO
TAM_MUTACAO = 5%TAM_POPULACAO
PESO_MAXIMO = 8000
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
populacao = gerarPopulacaoInicial(TAM_POPULACAO)
while geracao < NUM_GERACOES:
    populacao = sorted(populacao, key=lambda x: x[POSICAO_FITNESS], reverse=True)
    melhores_resultados = selecionarMenoresFitness(populacao, TAM_ELITE)
    piores_resultados = selecionarMaioresFitness(populacao, TAM_MUTACAO)
    nova_geracao.clear()
    nova_geracao = inicializarGeracao(gerarFilhos(populacao))
    nova_geracao.extend(melhores_resultados)
    piores_resultados = mutar(piores_resultados)
    nova_geracao.extend(piores_resultados)
    nova_geracao = completarPopulacao(nova_geracao)
    nova_geracao = sorted(nova_geracao, key=lambda x: x[POSICAO_FITNESS], reverse=True)
    melhorResultado(nova_geracao)
    populacao = nova_geracao
    geracao += 1
print("Melhor resultado global:")
print(melhor_resultado)
print("Resultado iteração final:")
print(nova_geracao[0])
print("Tempo de execução: {:.1f}".format(time.time()-tempo_o))