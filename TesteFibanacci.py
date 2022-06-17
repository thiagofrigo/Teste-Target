# 2)Dado a sequência de Fibonacci, onde se inicia por 0 e 1 e o próximo valor sempre será a soma dos 2 valores
# anteriores (exemplo: 0, 1, 1, 2, 3, 5, 8, 13, 21, 34...), escreva um programa na linguagem que desejar onde,
# informado um número, ele calcule a sequência de Fibonacci
# e retorne uma mensagem avisando se o número informado pertence ou não a sequência.

inicial = [0,1]
#Função para calcular a sequencia de Fibonacci
def fibonacci(num):
    i = 0
    while inicial[-1]<num:
        inicial.append(inicial[i]+inicial[i+1])
        i = i +1
    print(inicial)

#Verifica se o número digitado faz parte da sequencia
def verificanum(num):
    if numero in inicial:
        print(f'O número {numero} faz parte da sequencia')
    else:
        print(f'O número {numero} não faz parte da sequencia')

#Recebendo o número que será utilizado e executando as funções
numero = int(input("Digite um número para verificar se ele esta na sequencia de Fibonacci: "))
fibonacci(numero)
verificanum(numero)