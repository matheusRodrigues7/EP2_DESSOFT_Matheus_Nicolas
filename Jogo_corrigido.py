from time import sleep 
import functions
import random
print('Jogo de Dominó')
print('='*30)
print('    Por Matheus e Nicolas     ')
print('='*30)

print('=> Design de Software')

print('Bem-vindo(a) ao jogo de Dominó! O objetivo desse jogo é ficar sem peças na sua mão antes dos outros jogadores.')
print('Vamos começar!!!')
continuar= 'S'
while continuar == 'S' or continuar == 's':
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

    pecas = functions.cria_pecas()
    call = functions.inicia_jogo(n_jogadores,pecas)
    mesa = call['mesa']
    monte = call['monte']
    jogadores = call['jogadores']
    soma = functions.cria_dic_soma(n_jogadores)
    passe=0

    indice_1j = random.randint(0,n_jogadores-1) #Sorteando o primeiro jogador

    while indice_1j <= n_jogadores:
        Tratamento_possiveis = True
        if indice_1j == n_jogadores:
            indice_1j = 0

        print(f'\nMESA: \n{functions.print_mesa(mesa)}\n')

        pecas_jogador = jogadores[indice_1j]

        possiveis = functions.posicoes_possiveis(mesa,pecas_jogador)

        nao_tem_peca = True
        while nao_tem_peca:
            if len(possiveis) == 0 and len(monte) == 0:
                break
                
            elif len(possiveis) == 0:
                if len(monte)>0:
                    qtde_pecas = len(pecas_jogador)
                    if indice_1j == 0:
                        print(f'Jogador: Você com {qtde_pecas} peça(s)')
                        print('Não tem peças possíveis. PEGANDO DO MONTE!')
                        input('[pressione ENTER]')
                    else:
                        print(f'Jogador: {indice_1j+1} com {qtde_pecas} peça(s)')
                        print('Não tem peças possíveis. PEGANDO DO MONTE!')

                    print(f'\nMESA: \n{functions.print_mesa(mesa)}\n')

                    pecas_jogador.append(monte[0])
                    monte.remove(monte[0])
                    possiveis = functions.posicoes_possiveis(mesa,pecas_jogador)
            else:
                nao_tem_peca = False
        
        qtde_pecas = len(pecas_jogador)

        if len(possiveis) > 0:
            peca = pecas_jogador[possiveis[0]]

        if indice_1j == 0:
            possiveis1 = []
            for indice in possiveis: 
                possiveis1.append(indice + 1)
                
            print (f'Jogador: Você com {qtde_pecas} peça(s)')
            print(functions.print_pecas(pecas_jogador))
            
            if len(possiveis) > 0:
                print(f'Peças possíveis: {possiveis1}')
                while Tratamento_possiveis or escolha_peca not in possiveis1:
                    escolha_peca = possiveis1[0]
                    try:
                        escolha_peca = int(input('Escolha a peça: '))
                        Tratamento_possiveis = False
                    except ValueError:
                        print('Posição inválida!')
                        Tratamento_possiveis=True
                    if escolha_peca not in possiveis1:
                        print('Posição inválida!')
                    print(f'Peças possíveis: {possiveis1}')
                peca = pecas_jogador[escolha_peca-1]
        
        else:
            print(f'Jogador: {indice_1j+1} com {qtde_pecas} peça(s)')
        
        # se o jogador n tiver peças e o monte estiver vazio
        if len(possiveis) == 0 and len(monte) == 0:
            print('Não tem peças possíveis. MONTE VAZIO - PULANDO A VEZ!')
            if indice_1j == 0: 
                input('[pressione ENTER]')
            passe += 1
            print('Passe: ', passe)
            indice_1j += 1
            if passe == n_jogadores:
                break
            continue

        print(f'Colocou: {functions.print_peca(peca)}')
        pecas_anteriores= pecas_jogador
        pecas_jogador.remove(peca)

        # redefinindo mesa
        mesa_anterior = mesa[:]
        mesa = functions.adiciona_na_mesa(peca,mesa)
        mesa_posterior = mesa[:]
        
        if len(mesa_anterior) < len(mesa_posterior):
            passe = 0

        if len(pecas_jogador) == 0:
            break

        indice_1j += 1

    # somando os pontos de cada jogador
    for i in range (n_jogadores):
        pontos = functions.soma_pecas(jogadores[i])
        soma[i] += pontos

    vencedor = functions.verifica_ganhador(jogadores)
    
    if len(monte) == 0 and passe == n_jogadores:
        print('TERMINOU SEM BATIDA! \nContabilizando peças...')
        for i in range(n_jogadores):
            if soma[i]==min(soma.values()):
                vencedor = i

    for jogador,pontos in soma.items():
        if jogador == 0:
            print(f'\nJogador: Você com {len(jogadores[jogador])} peças(s) e {pontos} pontos')
        else:
            print(f'Jogador: {jogador+1} com {len(jogadores[jogador])} peças(s) e {pontos} pontos')

    if vencedor == 0:
        print('\nVocê ganhou, parabens!')
    else:
        print(f'\nJogador {vencedor+1} ganhou!')

    continuar = input('\nQuer jogar novamente? [S/N] ')




