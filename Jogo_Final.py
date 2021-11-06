from time import sleep 
from functions import *
import random
print('{:^100}'.format('Jogo de dominó'))
print('='*100)
print('{:^100}'.format('Por Matheus e Nicolas'))
print('='*100)
print('=> Design de Software')
print('Bem-vindo(a) ao jogo de Dominó! O objetivo desse jogo é ficar sem peças na sua mão antes dos outros jogadores.')
print('Vamos começar!!!')

continuar= 'S'
while continuar == 'S' or continuar == 's':
    # tratamento de erro de entrada do usuário
    Tratamento = True
    while Tratamento or (n_jogadores < 2 or n_jogadores > 4):
        n_jogadores=2
        try:
            n_jogadores = int(input('Quantos jogadores? (2-4) '))
            Tratamento = False
        except ValueError:
            print('Digito inválido')
            Tratamento = True
        if n_jogadores < 2 or n_jogadores > 4:
            print('Digito inválido')

    pecas = cria_pecas()
    call = inicia_jogo(n_jogadores,pecas)
    mesa = call['mesa']
    monte = call['monte']
    jogadores = call['jogadores']
    soma = cria_dic_soma(n_jogadores)
    passe = 0

    jogador = random.randint(0,n_jogadores-1) #Sorteando o primeiro jogador

    while jogador <= n_jogadores:
        Tratamento_possiveis = True # variável p tratar o erro lá na frente, caso ocorra
        if jogador == n_jogadores:
            jogador = 0 

        print(f'\nMESA: \n{print_mesa(mesa)}\n')

        pecas_jogador = jogadores[jogador]

        possiveis = posicoes_possiveis(mesa,pecas_jogador)

        nao_tem_peca = True
        while nao_tem_peca:
            if len(possiveis) == 0 and len(monte) == 0:
                break
                
            elif len(possiveis) == 0: 
                if len(monte)>0:
                    qtde_pecas = len(pecas_jogador)
                    if jogador == 0: # se for 'você'
                        print(f'Jogador: Você com {qtde_pecas} peça(s)')
                        print(print_pecas(pecas_jogador))
                        print('Não tem peças possíveis. PEGANDO DO MONTE!')
                        input('[pressione ENTER]')
                    else:
                        print(f'Jogador: {jogador+1} com {qtde_pecas} peça(s)')
                        print('Não tem peças possíveis. PEGANDO DO MONTE!')
                        sleep(2)
                    
                    print(f'\nMESA: \n{print_mesa(mesa)}\n')

                    pecas_jogador.append(monte[0])
                    monte.remove(monte[0])
                    possiveis = posicoes_possiveis(mesa,pecas_jogador)
            else:
                nao_tem_peca = False
        
        qtde_pecas = len(pecas_jogador)

        if len(possiveis) > 0:
            peca = pecas_jogador[possiveis[0]]

        if jogador == 0: # se for 'você'
            possiveis1 = []
            for indice in possiveis: 
                possiveis1.append(indice + 1)
            
            print (f'Jogador: Você com {qtde_pecas} peça(s)')
            print(print_pecas(pecas_jogador))

            if len(possiveis1) > 0:
                print(f'Peças possíveis: {possiveis1}')
                # tratamento de erro de entrada do usuário
                while Tratamento_possiveis or escolha_peca not in possiveis1:
                    escolha_peca = possiveis1[0]
                    try:
                        escolha_peca = int(input(f'Escolha a peça: '))
                        Tratamento_possiveis = False
                    except ValueError:
                        print(f'Posição inválida! Possíveis: {possiveis1} ')
                        Tratamento_possiveis=True
                    if escolha_peca not in possiveis1:
                        print(f'Posição inválida! Possíveis: {possiveis1} ')

                peca = pecas_jogador[escolha_peca-1]
        
        else:
            print(f'Jogador: {jogador+1} com {qtde_pecas} peça(s)')
        
        # se o jogador n tiver peças e o monte estiver vazio
        if len(possiveis) == 0 and len(monte) == 0:
            print('Não tem peças possíveis. MONTE VAZIO - PULANDO A VEZ!')
            if jogador == 0: 
                input('[pressione ENTER]')
            sleep(2)
            passe += 1
            jogador += 1
            if passe == n_jogadores: # se todos passarem, sai do loop
                break
            continue

        print(f'Colocou: {print_peca(peca)}')
        pecas_anteriores= pecas_jogador
        pecas_jogador.remove(peca)

        mesa_anterior = mesa[:]
        mesa = adiciona_na_mesa(peca,mesa) # redefinindo mesa
        mesa_posterior = mesa[:]
        
        if len(mesa_anterior) < len(mesa_posterior): # se a peça foi colocada
            passe = 0

        if len(pecas_jogador) == 0: # se o jogador n tiver mais peças (ganhou), sai do loop
            break

        sleep(2)

        jogador += 1

    sleep(2) 

    print('\nFINAAAAAL DE JOGO!\n')

    # somando os pontos de cada jogador
    for i in range (n_jogadores):
        pontos = soma_pecas(jogadores[i])
        soma[i] += pontos #add no dicionário soma

    for j,p in soma.items(): # para jogador e pontos no dicionario 
        if j == 0:
            if len(jogadores[j]) == 0:
                print(f'Jogador: Você sem peças e 0 pontos')
            else:
                print(f'Jogador: Você com {print_pecas(jogadores[j])}e {p} pontos')

        elif len(jogadores[j]) == 0:
            print(f'Jogador: {j+1} sem peças e 0 pontos')

        else:
            print(f'Jogador: {j+1} com {print_pecas(jogadores[j])}e {p} pontos')
    
    vencedor = verifica_ganhador(jogadores)

    if vencedor == 0:
        vencedor = 'Você'
    else:
        vencedor += 1 

    vencedores = []
    if len(monte) == 0 and passe == n_jogadores: # se o monte está vazio e todos passaram, n teve batida
        print('\nTERMINOU SEM BATIDA! \nContabilizando peças...')
        sleep(2)
        for i in range(n_jogadores):
            if soma[i] == min(soma.values()):
                vencedores.append(i)

    sleep(2)

    if len(vencedores) > 0: # se ninguem bateu
        print(f'\nVENCEDOR(ES): {print_vencedor(vencedores)}')
    else: # se um bater
        print(f'\nVENCEDOR(ES): [{vencedor}]')

    sleep(1)

    continuar = input('\nQuer jogar novamente? [S/N] ')




