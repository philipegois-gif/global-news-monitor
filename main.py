from fetcher import buscar_titulos
from analyzer import analisar_frequencia

def executar_ponte_global():
    print("\n" + "="*40)
    print(" BRIDGE NEWS AI - MONITOR DE CONVERGÊNCIA")
    print("="*40)
    
    # 1. Busca os dados
    print(" Coletando notícias internacionais e nacionais...")
    titulos = buscar_titulos()
    
    # 2. Analisa os dados
    print(" Analisando tendências de hoje...")
    tendencias = analisar_frequencia(titulos)
    
    # 3. Exibe o resultado genial
    print("\n TOP TEMAS EM ALTA NO MOMENTO:")
    for i, (palavra, freq) in enumerate(tendencias, 1):
        print(f"{i}º | {palavra.upper()} (mencionado {freq}x)")
    
    print("\n" + "="*40)
    print(" Processamento concluído com sucesso!")

if __name__ == "__main__":
    executar_ponte_global()
