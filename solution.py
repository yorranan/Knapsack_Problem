import random

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
   TAMANHO_CROMOSSOMO = 11
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

def selecionarMenores(populacao, tamanho):
    menores_resultados = []
    i = 0
    while i < tamanho:
        try:
            menores_resultados.append(populacao.pop())
        except IndexError:
            print('A lista está vazia')
        i += 1
    return menores_resultados

def selecionarMaiores(populacao, tamanho):
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
    while len(populacao) >= 2:
        pai = populacao.pop(random.choice(range(len(populacao))))
        mae = populacao.pop(random.choice(range(len(populacao))))
        filho = pai[1][:6] + mae[1][6:]
        filha = mae[1][:6] + pai[1][6:]
        filhos.append(filha)
        filhos.append(filho)

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
    melhor = populacao[0]
    return melhor
    
TAM_POPULACAO = 20
TAM_ELITE = 25%TAM_POPULACAO
TAM_CROSSOVER = 50%TAM_POPULACAO
TAM_MUTACAO = 25%TAM_POPULACAO
PESO_MAXIMO = 12000
POSICAO_INDEX = 0
POSICAO_CROMOSSOMO = 1
POSICAO_FITNESS = 2
geracao = 0
max_index = 0
nova_geracao = []
populacao = []
melhor_resultado = None

populacao = gerarPopulacaoInicial(TAM_POPULACAO)
populacao = sorted(populacao, key=lambda x: x[POSICAO_FITNESS], reverse=True)
imprimirPopulacao("População Inicial:", populacao)
melhores_resultados = selecionarMenores(populacao, TAM_ELITE)
piores_resultados = selecionarMaiores(populacao, TAM_MUTACAO)
nova_geracao = inicializarGeracao(gerarFilhos(populacao))
nova_geracao.extend(melhores_resultados)
nova_geracao = completarPopulacao(populacao)
imprimirPopulacao("Populacao Final:",nova_geracao)
print("Melhor resultado ")
print(melhorResultado(melhores_resultados))
    