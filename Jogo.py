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
#while algo:
if len(mesa) == 0:
    print('MESA: \n')
else:
    print(f'MESA: \n {mesa}')
quantidade_pecas = len(call['jogadores'][indice_1j])


# Chamar a função add peças na mesa
# Chamar a função posições possíveis

possiveis = functions.posicoes_possiveis(mesa,call['jogadores'][indice_1j])

possiveis1 = []
for indice in possiveis: 
    possiveis1.append(indice + 1)

print (f'Jogador: {jogador_inicia} com {quantidade_pecas} peça(s)')

peca = int(input('Escolha a peça: '))

while peca not in possiveis1:
    print('Posição inválida!')
    peca = int(input(f'Escolha a peça [{possiveis1}] '))

print(call['monte'])
print (call['jogadores'])