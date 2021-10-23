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