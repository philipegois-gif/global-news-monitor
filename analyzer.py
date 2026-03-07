def limpar_texto(texto):
    # Lista de palavras para ignorar (Stopwords)
    ignorar = ['o', 'a', 'os', 'as', 'de', 'do', 'da', 'em', 'um', 'uma', 'com', 'no', 'na', 'para', 'e', 'é']
    palavras = texto.lower().replace(',', '').replace(':', '').split()
    return [p for p in palavras if p not in ignorar and len(p) > 3]

def analisar_frequencia(lista_titulos):
    contagem = {}
    for titulo in lista_titulos:
        palavras = limpar_texto(titulo)
        for p in palavras:
            contagem[p] = contagem.get(p, 0) + 1
    
    # Ordena pelas mais frequentes
    ordenado = sorted(contagem.items(), key=lambda x: x[1], reverse=True)
    return ordenado[:5]

if __name__ == "__main__":
    print(" Analisador pronto para processar dados...")
    # Teste rápido
    teste = ["Trump ataca Irã", "Conflito no Irã aumenta", "Brasil observa Irã"]
    print(f"Top Palavras: {analisar_frequencia(teste)}")
