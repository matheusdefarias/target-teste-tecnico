# Inicialização das variáveis
INDICE = 13  # O valor limite para K
SOMA = 0     # Variável que armazenará a soma dos valores de K
K = 0         # Contador que será incrementado em cada iteração do laço

# Laço "Enquanto" (equivalente ao "while" em Python)
while K < INDICE:  # Enquanto K for menor que INDICE (13)
    K = K + 1      # Incrementa K em 1
    SOMA = SOMA + K  # Soma o valor de K a SOMA

# Após o término do laço, imprimimos o valor final de SOMA
print(SOMA)  # A impressão de SOMA nos dará o resultado final
