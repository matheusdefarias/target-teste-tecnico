# Função para calcular a sequência de Fibonacci até um certo número
def fibonacci(n):
    # Inicializa os dois primeiros termos da sequência de Fibonacci
    fib_sequence = [0, 1]
    
    # Calcula a sequência até o número desejado
    while fib_sequence[-1] < n:
        # Adiciona o próximo número da sequência (soma dos dois últimos)
        fib_sequence.append(fib_sequence[-1] + fib_sequence[-2])
    
    return fib_sequence

# Função para verificar se um número pertence à sequência de Fibonacci
def verificar_fibonacci(num):
    # Chama a função fibonacci para obter a sequência até o número informado
    fib_sequence = fibonacci(num)
    
    # Verifica se o número informado está na sequência de Fibonacci
    if num in fib_sequence:
        return f'O número {num} pertence à sequência de Fibonacci.'
    else:
        return f'O número {num} não pertence à sequência de Fibonacci.'

# Solicita ao usuário para digitar um número
numero = int(input("Digite um número para verificar se pertence à sequência de Fibonacci: "))

# Chama a função de verificação e imprime o resultado
resultado = verificar_fibonacci(numero)
print(resultado)
