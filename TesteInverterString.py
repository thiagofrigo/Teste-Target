#5) Escreva um programa que inverta os caracteres de um string.

#Recebendo a palavra e criando uma lista para armazenar suas letras
palavra = input("Digite uma palavra: ")
contrario = []
j = 0
#Colocando as letras da palavra na ordem inversa na listra criada
for i in range(len(palavra)):
    j = j - 1
    contrario.append(palavra[j])

#Usando a função join para concatenar a lista em uma string
AoContrario = ''.join(contrario)
print(AoContrario)