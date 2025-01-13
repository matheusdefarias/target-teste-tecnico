# Função para inverter uma string
def inverter_string(s):
    # Inicializa uma variável vazia para armazenar a string invertida
    string_invertida = ""
    
    # Percorre a string de trás para frente e adiciona cada caractere à nova string
    for i in range(len(s) - 1, -1, -1):
        string_invertida += s[i]
    
    return string_invertida

# Função principal
def main():
    # Entrada da string
    string = input("Digite uma string para inverter: ")
    
    # Chama a função para inverter a string
    resultado = inverter_string(string)
    
    # Exibe a string invertida
    print("String invertida:", resultado)

# Executa o programa
if __name__ == "__main__":
    main()
