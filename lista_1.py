#PLANEJAMENTO DE VIAGEM (CONVERSÃO DE MOEDAS)
#cotação do dólar 13/10 = R$5,61
moeda = int(input('Digite 1 se deseja converter de real para dólar ou digite 2 se quiser converter de dólar para real: \n'))

if moeda == 1:
    valor = float(input('Digite o valor que possui em real: '))
    convertido_dolar = valor / 5.61
    print(f'Você possui {valor:.2f} reais, o que equivale a {convertido_dolar:.2f} dólares.')
elif moeda == 2:    
    valor = float(input('Digite o valor que possui em dólar: '))
    convertido_real= valor * 5.61
    print(f'Você possui {valor:.2f} dólares, o que equivale a {convertido_real:.2f} reais.')
else:
    print('Opção inválida')

###############################################################################
#CÁLCULO DO CONSUMO DE COMBUSTÍVEL
distancia = float(input('Digite a distância que será percorrida, em km: '))
consumo = float(input('Digite a média de km por litro em seu carro: '))
valor = float(input('Digite o valor do litro do combustível considerado para a média acima: '))

litros_combustivel = distancia / consumo
valor_combustivel = litros_combustivel * valor
print(f'Serão necessários {litros_combustivel:.2f} litros de combustível para percorrer a distância informada e será gasto um total de {valor_combustivel:.2f} reais em combustível.')

###############################################################################
#GERADOR DE SENHAS PERSONALIZADAS
nome = input('Digite seu nome completo: \n')
data = input('Digite sua data de nascimento de acordo com o formato dd/mm/aaaa: \n')

senha = nome[0:3] + data[6:8] + ' ' + str(len(nome)) + '!'
print('Senha Gerada: ' + senha.upper())

###############################################################################
#CÁLCULO DE JUROS SIMPLES (APLICAÇAO FINANCEIRA)
capital_inicial = float(input('Digite o valor que pretende investir (em real): \n'))
taxa_juros = float(input('Digite a taxa de juros anual: \n')) / 100 
escolha = int(input('Digite 1 caso vá investir em anos ou digite 2 caso seja em meses. \n'))

if escolha == 1:
    tempo = int(input('Digite o número de anos que o dinheiro ficará investido: \n'))
elif escolha == 2:
    tempo = int(input('Digite o número de meses que o dinheiro ficará investido: \n')) / 12
else:
    print('Opção inválida')
    exit()

montante_final = capital_inicial * (1 + taxa_juros) ** tempo

print(f'O valor final que terá, após o investimento é de {montante_final:.2f}')

###############################################################################
#DESAFIO: VERIFICAÇÃO DE ID VÁLIDO
cpf = input('DIgite o CPF ou CNPJ que deseja saber se é válido (utilize ., - ou /): \n')

if len(cpf) == 14 and cpf[3] == '.' and cpf[7] == '.' and cpf[11] == '-':
    print('CPF Válido')
elif len(cpf) == 18 and cpf[2] == '.' and cpf[6] == '.' and cpf[10] == '/' and cpf[15] == '-':
    print('CNPJ Válido')
else:
    print('CPF ou CNPJ inválido')