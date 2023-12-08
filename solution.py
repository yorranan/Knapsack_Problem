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

geracao = 0
tam_populacao = 10
gerarPopulacao(tam_populacao)

