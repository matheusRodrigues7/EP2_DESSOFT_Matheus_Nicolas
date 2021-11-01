# CRIAR PEÇAS
import random
def cria_pecas():
    pecas = []
    i = 0 
    while i < 7:
        j = i
        while j < 7:
            pecas.append([i,j])
            j += 1
        i += 1
    random.shuffle(pecas)
    return pecas
    
# INICIANDO O JOGO
def inicia_jogo(n_jogadores,lista_pecas):

    dicionario = {
	'jogadores': {},
	'monte': [],
	'mesa': []
}

    i = 0 
    while i < n_jogadores:
        # criando uma lista vazia de peças para o jogador 'i'
        dicionario['jogadores'][i] = []
        for peca in lista_pecas:
            # add p o jogador e removendo o primeiro termo da lista de peças até o jogador tiver 7 peças
            while len(dicionario['jogadores'][i]) < 7:
                dicionario['jogadores'][i].append(lista_pecas[0])
                lista_pecas.remove(lista_pecas[0])
        i += 1
    
    #monte é oq sobrou da lista
    dicionario['monte'] = lista_pecas
    
    return dicionario

# QUEM GANHOU? 
def verifica_ganhador(jogadores):
    for jogador,pecas in jogadores.items():
        if len(pecas) == 0:
            return jogador
    return -1

# SOMA PEÇAS
def soma_pecas(pecas):
    soma = 0
    for peca in pecas:
        soma += sum(peca) 
    return soma

# POSIÇÕES POSSÍVEIS DA MÃO
def posicoes_possiveis(mesa,pecas):

    possiveis = []
    if len(mesa) == 0:
        possiveis = [0,1,2,3,4,5,6]
    else:
        for peca in pecas:
            for n in peca:
                if n == mesa[0][0] or n == mesa[-1][1]:
                    indice = pecas.index(peca)
                    if indice not in possiveis:
                        possiveis.append(indice)
        
    return possiveis

# ADICIONA PEÇA A MESA

def adiciona_na_mesa(peca,mesa):
    if len(mesa) == 0:
        mesa.append(peca)
    
    elif len(mesa) == 1 and mesa[0][0] == mesa[0][1] and mesa[0][1] == peca[0]:
        peca.reverse()
        mesa.insert(0,peca)
    
    elif len(mesa) == 1 and mesa[0][0] == mesa[0][1] and mesa[0][0] == peca[1]:
        mesa.insert(0,peca)

    elif peca[0] == mesa[-1][1]:
        mesa.append(peca)
    
    elif peca[0] == mesa [0][0]:
        peca.reverse()
        mesa.insert(0,peca)
    
    elif peca[1] == mesa[-1][1]:
        peca.reverse()
        mesa.append(peca)

    elif peca[1] == mesa[0][0]:
        mesa.insert(0,peca)

    return mesa

def print_pecas(pecas):
    s= ''
    for p in pecas:
        s += '[' + f'{p[0]}' + '|' + f'{p[1]}' + ']'
        s += ' '
    return s

def print_mesa(mesa):
    s= ''
    for p in mesa:
        s += '[' + f'{p[0]}' + '|' + f'{p[1]}' + ']'
    return s