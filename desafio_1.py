renda = float(input('Insira sua renda mensal em reais: '))
despesa_1 = float(input('Insira o valor de suas despesas desse mês: '))
despesa_2 = float(input('Insira o valor de suas despesas do mês passado: '))
despesa_3 = float(input('Insira o valor de suas despesas do mês retrasado: '))

media_despesas = (despesa_1 + despesa_2 + despesa_3) / 3
saldo_anual = renda * 12 - media_despesas * 12

print(f'O valor de seu saldo final esperado é de {saldo_anual:.2f} reais, baseado em uma média de {media_despesas:.2f} reais de despesas por mês.')