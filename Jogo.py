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

indice_1j = random.randint(0,n_jogadores-1) #Indice do primeiro jogador.
if indice_1j == 0:
    jogador_inicia = 'Você'
else:
    jogador_inicia=indice_1j

pecas = functions.cria_pecas()
call = functions.inicia_jogo(n_jogadores,pecas)
mesa = call['mesa']
while indice_1j <= n_jogadores:
    indice_1j+=1
    if indice_1j==n_jogadores:
        indice_1j=0
    if len(mesa) == 0:
        print('MESA: \n')
    else:
        print(f'MESA: \n {mesa}')

    pecas_jogador = call['jogadores'][indice_1j]
    qtde_pecas = len(pecas_jogador)

    # Chamar a função add peças na mesa
    # Chamar a função posições possíveis

    possiveis = functions.posicoes_possiveis(mesa,pecas_jogador)

    possiveis1 = []
    for indice in possiveis: 
        possiveis1.append(indice + 1)

    peca = pecas_jogador[possiveis[0]]

    if jogador_inicia == 'Você':
        print(possiveis1)
        print(pecas_jogador)
        escolha_peca = int(input('Escolha a peça: '))

        while escolha_peca not in possiveis1:
            print('Posição inválida!')
            escolha_peca = int(input(f'Escolha a peça {possiveis1} '))

        peca = pecas_jogador[possiveis[escolha_peca-1]]

    pecas_jogador.remove(peca)
    print (f'Jogador: {jogador_inicia} com {qtde_pecas} peça(s)')
    print(f'Colocou: {peca}')

    # redefinindo mesa
    mesa = functions.adiciona_na_mesa(peca,mesa)
    print(f'MESA: \n{mesa}')

    print(call['monte'])
    print (call['jogadores'])