import random

def gerarPopulacao(tamanho):
    populacao = []
    for i in range(tamanho):
        populacao.append(preencherCromossomo())
    
    return populacao

def preencherCromossomo():
    TAM = 12
    cromossomo = []*TAM 
    n = 2
    while n <= 4096:
        cromossomo.append(random.randrange(0, n))
        n *= 2
    return cromossomo

def calcularPesoTotal(individuo, pesos):
    peso_total = 0
    for i, j in zip(individuo, pesos):
        peso_total += i*j
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

def selecionarIndividuos(populacao, resultados, tam_selecionados):
    resultados.sort()
    selecionados = []
    for i in range(tam_selecionados):
        selecionados.append(populacao[resultados[i][1]])

def crossover(selecionados):
    nova_populacao = []
    while selecionados.len() >= 1:
        indice = random.choice(range(len(selecionados)))
        pai = selecionados.pop(indice)
        indice = random.choice(range(len(selecionados)))
        mae = selecionados.pop(indice)

        filho = pai[:6] + mae[6:]
        filha = mae[:6] + pai[6:]
        nova_populacao.append(filho)
        nova_populacao.append(filha)

    return nova_populacao

def mutacao(populacao, taxa_mutacao):
    para_mutar = []
    # escolhe 3 elementos aleatórios da população sem repetição e os remove da lista original
    para_mutar = random.sample(populacao, taxa_mutacao)
    for i in para_mutar:
        populacao.remove(i)
    # aplica uma mutação em cada elemento escolhido, de acordo com a taxa de mutação
    for i in range(len(para_mutar)):
        # aqui você pode definir como será a mutação, por exemplo, trocando um bit aleatório
        bit = random.randint(0, len(para_mutar[i]) - 1) # escolhe um bit aleatório
        prob = random.random() # gera um número aleatório entre 0 e 1
        if prob < taxa_mutacao: # se a probabilidade for menor que a taxa de mutação, troca o bit
            para_mutar[i][bit] = 1 - para_mutar[i][bit] # troca 0 por 1 e vice-versa
    # retorna a lista modificada
    return para_mutar
