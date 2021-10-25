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

indice_1j=random.randint(0,n_jogadores-1) #Indice do primeiro jogador.
if indice_1j==0:
    jogador_inicia='Você'
else:
    jogador_inicia=indice_1j

pecas=functions.cria_pecas()
call=functions.inicia_jogo(n_jogadores,pecas)
mesa= call['mesa']
while algo:
    quantidade_pecas= len(call['jogadores'][indice_1j])
    print (f'MESA:{mesa}')

    print (f'Jogador: {jogador_inicia} com {quantidade_pecas} peças')



    print(call['monte'])
    print (call['jogadores'])