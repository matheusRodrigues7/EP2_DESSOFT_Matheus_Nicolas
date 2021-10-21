print('Jogo de Dominó')
print('Por Matheus e Nicolas')
print('=> Design de Software')

print('Bem-vindo(a) ao jogo de Dominó! O objetivo desse jogo é ficar sem peças na sua mão antes dos outros jogadores.')
print('Vamos começar!!!')

n_jogadores = int(input('Quantos jogadores? (2-4)'))

while n_jogadores > 4 or  n_jogadores < 2:
    n_jogadores = int(input('Quantos jogadores? (2-4)'))