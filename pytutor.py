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

import functions
import random
print('Jogo de Dominó')

print('='*30)
print('    Por Matheus e Nicolas     ')
print('='*30)

print('=> Design de Software')

print('Bem-vindo(a) ao jogo de Dominó! O objetivo desse jogo é ficar sem peças na sua mão antes dos outros jogadores.')
print('Vamos começar!!!')

n_jogadores = int(input('Quantos jogadores? (2-4) '))

while n_jogadores > 4 or n_jogadores < 2:
    print('Número inválido!')
    n_jogadores = int(input('Quantos jogadores? (2-4)'))

pecas = functions.cria_pecas()
call = functions.inicia_jogo(n_jogadores,pecas)
mesa = call['mesa']
monte = call['monte']
jogadores = call['jogadores']
soma = {0:0,1:0,2:0,3:0}
passe=0
mesa_anterior=[]
mesa_posterior=[]
indice_1j = random.randint(0,n_jogadores-1) #Indice do primeiro jogador.
if indice_1j == 0:
    jogador_inicia = 'Você'
else:
    jogador_inicia=indice_1j

while indice_1j <= n_jogadores:
    
    if len(mesa_anterior)<len(mesa_posterior):
        passe = 0
        print(passe,'PASSEEEEEEEE')

    if indice_1j == n_jogadores:
        indice_1j = 0

    if len(mesa) == 0:
        print('MESA: \n')
    else:
        print(f'MESA: \n {mesa}')

    pecas_jogador = call['jogadores'][indice_1j]

    # Chamar a função add peças na mesa
    # Chamar a função posições possíveis

    possiveis = functions.posicoes_possiveis(mesa,pecas_jogador)

    nao_tem_peca = True
    if len(possiveis)==0:
        if n_jogadores==4:
            indice_1j+=1
            continue
        else:
            while nao_tem_peca:
                if len(possiveis)==0 and len(monte)==0:
                    nao_tem_peca=False
                elif len(possiveis)==0:
                    if len(monte)>0:
                        print('comprou')
                        pecas_jogador.append(monte[0])
                        monte.remove(monte[0])
                        possiveis = functions.posicoes_possiveis(mesa,pecas_jogador)
                        print(monte) #Checagem
                else:
                    nao_tem_peca=False
            print(pecas_jogador)

    qtde_pecas = len(pecas_jogador)

    if len(possiveis)>0:
        peca = pecas_jogador[possiveis[0]]

    if indice_1j == 0:
        possiveis1 = []
        for indice in possiveis: 
            possiveis1.append(indice + 1)
            
        print (f'Jogador: Você com {qtde_pecas} peça(s)')
        print(pecas_jogador)
        print(possiveis1)
        escolha_peca = int(input('Escolha a peça: '))

        while escolha_peca not in possiveis1:
            print('Posição inválida!')
            escolha_peca = int(input(f'Escolha a peça {possiveis1} '))
        
        peca = pecas_jogador[escolha_peca-1]
    else:
        print(f'Jogador: {indice_1j+1} com {qtde_pecas} peça(s)')
        print(jogadores[indice_1j]) #CHECAGEM.

    print(f'Colocou: {peca}')
    pecas_anteriores= pecas_jogador
    pecas_jogador.remove(peca)

    # redefinindo mesa
    mesa_anterior=mesa
    mesa = functions.adiciona_na_mesa(peca,mesa)
    mesa_posterior=mesa
    '''print(f'MESA: \n{mesa}')'''
    
    if len(possiveis)==0 and len(monte)==0:
        print('passou')
        passe+=1
        
    if len(pecas_jogador)==0:
        for i in range (0,n_jogadores):
            soma[i]+=functions.soma_pecas(jogadores[i])
        print(soma)
        break
    if len(pecas_jogador)==0:
        break
    
    indice_1j += 1
    
vencedor = functions.verifica_ganhador(jogadores)
#(soma0<soma1 and soma0<soma2 and soma0<soma3)

if len(monte) == 0 and passe == n_jogadores:
    for jogador,s in soma.items():
        if s == min(soma.values()):
            if jogador == 0:
                print('Você ganhou parabens!!')
            else:
                print(f'Jogador {jogador} ganhou!')

if vencedor == 0:
    print('Você ganhou parabens!!')
if len(monte) == 0 and vencedor == -1:
    soma = functions.soma_pecas(pecas_jogador)



# FUNCIONALIDADE DE COMPRAR DO MONTE 
# CHAMAR A FUNÇÃO VENCEDOR




