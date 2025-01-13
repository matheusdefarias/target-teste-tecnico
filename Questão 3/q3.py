import json

# Função para carregar os dados do faturamento diário de um arquivo JSON
def carregar_dados(ficheiro):
    print(ficheiro)
    with open(ficheiro, 'r') as file:
        # Carrega os dados do JSON
        return json.load(file)

# Função para calcular o menor e maior faturamento, e o número de dias acima da média
def analisar_faturamento(faturamentos):
    # Filtra os dias com faturamento (desconsiderando valores 0 ou None)
    faturamentos_validos = [f for f in faturamentos if f > 0]
    
    if not faturamentos_validos:
        return None, None, 0
    
    # Calculando o menor e maior faturamento
    menor_faturamento = min(faturamentos_validos)
    maior_faturamento = max(faturamentos_validos)
    
    # Calculando a média mensal
    media_mensal = sum(faturamentos_validos) / len(faturamentos_validos)
    
    # Contando os dias com faturamento superior à média
    dias_acima_media = len([f for f in faturamentos_validos if f > media_mensal])
    
    return menor_faturamento, maior_faturamento, dias_acima_media

# Função principal
def main():
    # Caminho para o arquivo JSON contendo o faturamento diário
    arquivo_faturamento = r'./faturamento.json'  # Substitua pelo caminho correto
    
    # Carrega os dados do faturamento
    faturamentos = carregar_dados(arquivo_faturamento)
    
    # Chama a função de análise
    menor, maior, dias_acima_media = analisar_faturamento(faturamentos)
    
    # Exibe os resultados
    print(f'Menor faturamento: {menor}')
    print(f'Maior faturamento: {maior}')
    print(f'Dias com faturamento superior à média: {dias_acima_media}')

# Executa o programa
if __name__ == '__main__':
    main()
