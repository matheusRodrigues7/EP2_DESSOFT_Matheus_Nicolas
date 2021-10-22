def verifica_ganhador(jogadores):

    for jogador,pecas in jogadores.items():
        if len(pecas) == 0:
            return jogador
    
    return -1

def soma_pecas(pecas):

    soma = 0
    for peca in pecas:
        soma += sum(peca)
        
    return soma