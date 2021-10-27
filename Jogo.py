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

indice_1j = random.randint(0,n_jogadores-1) #Indice do primeiro jogador.
if indice_1j == 0:
    jogador_inicia = 'Você'
else:
    jogador_inicia=indice_1j

while indice_1j <= n_jogadores:
    
    if indice_1j == n_jogadores:
        indice_1j = 0

    if len(mesa) == 0:
        print('MESA: \n')
    else:
        print(f'MESA: \n {mesa}')

    pecas_jogador = call['jogadores'][indice_1j]
    qtde_pecas = len(pecas_jogador)

    # Chamar a função add peças na mesa
    # Chamar a função posições possíveis

    possiveis = functions.posicoes_possiveis(mesa,pecas_jogador)

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
    
    print(f'Colocou: {peca}')

    pecas_jogador.remove(peca)

    # redefinindo mesa
    mesa = functions.adiciona_na_mesa(peca,mesa)
    '''print(f'MESA: \n{mesa}')'''

    vencedor = functions.verifica_ganhador(jogadores)
    if len(monte) == 0 and vencedor == -1:
        soma = functions.soma_pecas(pecas_jogador)

    indice_1j += 1

    '''print(call['monte'])
    print (call['jogadores'])'''


# FUNCIONALIDADE DE COMPRAR DO MONTE 
# CHAMAR A FUNÇÃO VENCEDOR



