# Função para calcular os percentuais de representação de cada estado
def calcular_percentuais(faturamento_estados):
    # Calcula o faturamento total
    total_faturamento = sum(faturamento_estados.values())
    
    # Dicionário para armazenar os percentuais
    percentuais = {}
    
    # Calcula o percentual de cada estado
    for estado, faturamento in faturamento_estados.items():
        percentual = (faturamento / total_faturamento) * 100
        percentuais[estado] = percentual
    
    return percentuais

# Função principal
def main():
    # Dicionário com os valores de faturamento por estado
    faturamento_estados = {
        'SP': 67836.43,
        'RJ': 36678.66,
        'MG': 29229.88,
        'ES': 27165.48,
        'Outros': 19849.53
    }
    
    # Chama a função para calcular os percentuais
    percentuais = calcular_percentuais(faturamento_estados)
    
    # Exibe o percentual de representação de cada estado
    for estado, percentual in percentuais.items():
        print(f'O estado {estado} representa {percentual:.2f}% do faturamento total.')

# Executa o programa
if __name__ == '__main__':
    main()
