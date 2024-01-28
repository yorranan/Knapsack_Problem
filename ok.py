import random

TAMANHO_CROMOSSOMO = 7
PESO_MAXIMO = 13
TAMANHO_POPULACAO = int(input("Tamanho da Populacao : "))
TAX_CROSSOVER = int(input("Taxa de Crossover : "))%TAMANHO_POPULACAO
TAX_MUTACAO = int(input("Taxa de Mutacao : "))%TAMANHO_POPULACAO
NUM_GERACOES = int(input("Numero de Geracoes : "))
TAMANHO_ELITE = 20%TAMANHO_POPULACAO

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
    lista_de_valores = [2, 7, 3, 4, 5, 2, 6]
    for i, j in zip(cromossomo, lista_de_valores):
        fitness += i * j
    return fitness

def calcularPeso(cromossomo:list):
    peso = 0
    lista_de_pesos = [6, 3, 1, 7, 4, 2, 5]
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
    tax = TAX_CROSSOVER
    tam_lista = len(populacao)
    while tam_lista >= 2:
        pai = populacao.pop(random.choice(range(len(populacao))))
        mae = populacao.pop(random.choice(range(len(populacao))))
        filho = pai[1][:3] + mae[1][3:]
        filhos.append((0, filho, 0))
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

geracao = 0
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
    elite = selecionarElite(populacao)
    filhos = gerarFilhos(populacao)
    filhos = mutar(filhos)
    populacao.clear()
    populacao = elite + filhos + preencherPopulacao(TAMANHO_POPULACAO-len(elite)-len(filhos))
    populacao = avaliarPopulacao(populacao)
    geracao += 1

print("Final population after", NUM_GERACOES ,"generations:")
populacao.sort(key=lambda x: x[2], reverse=True)
for individuo in populacao:
    print(individuo)