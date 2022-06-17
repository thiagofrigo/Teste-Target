#4) Dado o valor de faturamento mensal de uma distribuidora, detalhado por estado:
#SP – R$67.836,43
#RJ – R$36.678,66
#MG – R$29.229,88
#ES – R$27.165,48
#Outros – R$19.849,53
#Escreva um programa na linguagem que desejar onde calcule o percentual de representação que cada estado teve dentro do valor total mensal da distribuidora.

#Somando o total do faturamento
totalFaturamento = 67.83643 + 36.67866 + 29.22988 + 27.16548 + 19.84953

#Encontrando as porcentagens correspondentes
sp = (67.83643*100)/totalFaturamento
rj = (36.67866*100)/totalFaturamento
mg = (29.22988*100)/totalFaturamento
es = (27.16548*100)/totalFaturamento
outros = (19.84953*100)/totalFaturamento
print(f'São Paulo corresponde a {sp:.2f}% do total mensal\n'
      f'Rio de Janeiro Corresponde a {rj:.2f}%,\n'
      f'Minas Gerais corresponde a {mg:.2f}%,\n'
      f'Espirito Santo corresponde a {es:.2f}%,\n'
      f'e os demais estados correspondem somados a {outros:.2f}% do total mensal')