def agente(pergunta):
    if 'vendas' in pergunta.lower():
        return 'Executar SQL de vendas'
    elif 'clientes' in pergunta.lower():
        return 'Executar SQL de clientes'
    else:
        return 'Não sei responder'