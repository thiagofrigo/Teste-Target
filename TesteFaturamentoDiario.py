#3) Dado um vetor que guarda o valor de faturamento diário de uma distribuidora, faça um programa, na linguagem que desejar,
# que calcule e retorne:
#• O menor valor de faturamento ocorrido em um dia do mês;
#• O maior valor de faturamento ocorrido em um dia do mês;
#• Número de dias no mês em que o valor de faturamento diário foi superior à média mensal.

import json
from statistics import mean

#lendo o arquivo json
with open("dados.json") as arquivoJson:
    dados = json.load(arquivoJson)


faturamento = []
#Extraindo apenas os valores numéricos do arquivo json
for i in dados:
    faturamento.append(i['valor'])

#Removendo os valores que correspondem a 0
try:
    while True:
        faturamento.remove(0)
except ValueError:
    pass

#Encontrando os valores máximos, mínimos e a média do faturamento
maiorValor = max(faturamento)
menorValor = min(faturamento)
media = mean(faturamento)

print(f'O menor faturamento do mês, excluindo os dias em que o faturamento foi 0, foi de: {menorValor:.2f}')
print(f'O maior faturamento do mês foi de: {maiorValor:.2f}')

#Contando quantas vezes os valores diarios foram maiores que a média
maiorMedia = 0
for i in range(len(faturamento)):
    if faturamento[i] > media:
        maiorMedia = maiorMedia + 1
print(f'O faturamente foi maior que a média mensal em {maiorMedia} dias')