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

# ADICIONA PEÇA NA MESA

def adiciona_na_mesa(peca,mesa):
    if len(mesa) == 0:
        mesa.append(peca)
    
    elif peca[0] == mesa[-1][1]:
        mesa.append(peca)
    
    # peça a esquerda
    elif peca[0] == mesa[0][0]:
        # inverte a peça 
        #peca.reverse()
        mesa.insert(0,[peca[1],peca[0]])

    elif peca[1] == mesa[-1][1]:
        #peca.reverse()
        mesa.append([peca[1],peca[0]])
    
    elif peca[1] == mesa[0][0]:
        mesa.insert(0,peca)

    return mesa

def print_peca(p):
    if p[0]==0:
        cor = f'\033[0;90m{p[0]}\033[m'
    if p[1]==0:
        cor2 = f'\033[0;90m{p[1]}\033[m'
    if p[0]==1:
        cor = f'\033[0;31m{p[0]}\033[m'
    if p[1]==1:
        cor2 = f'\033[0;31m{p[1]}\033[m'
    if p[0]==2:
        cor = f'\033[0;32m{p[0]}\033[m'
    if p[1]==2:
        cor2 = f'\033[0;32m{p[1]}\033[m'
    if p[0]==3:
        cor = f'\033[0;33m{p[0]}\033[m'
    if p[1]==3:
        cor2 = f'\033[0;33m{p[1]}\033[m'
    if p[0]==4:
        cor = f'\033[0;91m{p[0]}\033[m'
    if p[1]==4:
        cor2 = f'\033[0;91m{p[1]}\033[m'
    if p[0]==5:
        cor = f'\033[0;35m{p[0]}\033[m'
    if p[1]==5:
        cor2 = f'\033[0;35m{p[1]}\033[m'
    if p[0]==6:
        cor = f'\033[0;36m{p[0]}\033[m'
    if p[1]==6:
        cor2 = f'\033[0;36m{p[1]}\033[m'
            
    s = '[' + f'{cor}' + '|' + f'{cor2}' + ']'
    return s

def print_pecas(pecas):
    s= ''
    for p in pecas:
        if p[0]==0:
            cor = f'\033[0;90m{p[0]}\033[m'
        if p[1]==0:
            cor2 = f'\033[0;90m{p[1]}\033[m'
        if p[0]==1:
            cor = f'\033[0;31m{p[0]}\033[m'
        if p[1]==1:
            cor2 = f'\033[0;31m{p[1]}\033[m'
        if p[0]==2:
            cor = f'\033[0;32m{p[0]}\033[m'
        if p[1]==2:
            cor2 = f'\033[0;32m{p[1]}\033[m'
        if p[0]==3:
            cor = f'\033[0;33m{p[0]}\033[m'
        if p[1]==3:
            cor2 = f'\033[0;33m{p[1]}\033[m'
        if p[0]==4:
            cor = f'\033[0;91m{p[0]}\033[m'
        if p[1]==4:
            cor2 = f'\033[0;91m{p[1]}\033[m'
        if p[0]==5:
            cor = f'\033[0;35m{p[0]}\033[m'
        if p[1]==5:
            cor2 = f'\033[0;35m{p[1]}\033[m'
        if p[0]==6:
            cor = f'\033[0;36m{p[0]}\033[m'
        if p[1]==6:
            cor2 = f'\033[0;36m{p[1]}\033[m'
        s += '[' + f'{cor}' + '|' + f'{cor2}' + ']'
        s += ' '
    return s

def print_mesa(mesa):
    s = ''
    cor = ''
    cor2 = ''
    for p in mesa:
        if p[0]==0:
            cor = f'\033[0;90m{p[0]}\033[m'
        if p[1]==0:
            cor2 = f'\033[0;90m{p[1]}\033[m'
        if p[0]==1:
            cor = f'\033[0;31m{p[0]}\033[m'
        if p[1]==1:
            cor2 = f'\033[0;31m{p[1]}\033[m'
        if p[0]==2:
            cor = f'\033[0;32m{p[0]}\033[m'
        if p[1]==2:
            cor2 = f'\033[0;32m{p[1]}\033[m'
        if p[0]==3:
            cor = f'\033[0;33m{p[0]}\033[m'
        if p[1]==3:
            cor2 = f'\033[0;33m{p[1]}\033[m'
        if p[0]==4:
            cor = f'\033[0;91m{p[0]}\033[m'
        if p[1]==4:
            cor2 = f'\033[0;91m{p[1]}\033[m'
        if p[0]==5:
            cor = f'\033[0;35m{p[0]}\033[m'
        if p[1]==5:
            cor2 = f'\033[0;35m{p[1]}\033[m'
        if p[0]==6:
            cor = f'\033[0;36m{p[0]}\033[m'
        if p[1]==6:
            cor2 = f'\033[0;36m{p[1]}\033[m'

        s += '[' + f'{cor}' + '|' + f'{cor2}' + ']'
    return s

def cria_dic_soma(n_jogadores):
    soma = {}
    for i in range(n_jogadores):
        soma[i] = 0
    return soma

