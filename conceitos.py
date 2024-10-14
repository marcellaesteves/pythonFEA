#Tipos de dados
#int (integer) = 1, 2, 3, 100, 300
#float = 1.5, 9.3, 8.1
#str (strings) = textos entre aspas simples ou duplas
#bool (booleanos) = true/false

#Operações básicas
#adição = +
#subtração = -
#multiplicação = *
#divisão = /
#exponenciação = **
#divisão inteira = //
#módulo = %

#Operações comparativas
#igual a = ==
#maior que = >
#menor que = <
#maior ou igual = >=
#menor ou igual = <=
#diferente de = !=

#Métodos de String
teste = 'teste'
print(len(teste)) #Retorna o comprimento da string
print(teste.split()) #Divide a string em uma lista de acordo com o delimitador
print(teste.upper()) #Retorna a string toda em maiúscula
print(teste.lower()) #Retorna a string toda em minúscula
print(teste.strip()) #Retorna a string retirando possíveis espaços em branco no início e no fim
print(teste.startswith('xyz')) #Retorna se a string começa com xyz
print(teste.endswith('xyz')) #Retorna se a string termina com xyz
print(teste.find('xyz')) #Retorna se há xyz na string e o primeiro índice da onde aparece ou retorna -1, se não for encontrado
print(teste.replace('teste', 'olá')) #Substitui a palavra teste por olá, sempre que houver

#Exibição
nome = 'Marcella'
sobrenome = 'Esteves'
nome_completo = nome + " " + sobrenome
idade = 19
m1 = 5 * 2


print(nome_completo)
print(type(nome_completo))
print('Seu nome completo é {} e você tem {} anos.'.format(nome_completo, idade))
print(f'Seu nome completo é {nome_completo} e você tem {idade} anos.')
print(f'O resultado da multiplicação 2 * 5 é: {m1:.1f}') #O .1f delimita o número de casas decimais, nesse caso, 1

#Transformando tipos de dados
y = 3
x = 2
print(x + y)
print(str(x) + str(y))
print(float(x) + float(y))

#Acessando caracteres específicos
print(nome_completo[0])
print(nome_completo[-2])

#Inputs e Outputs
nome = input('Digite seu primeiro nome: ')
idade = int(input('Qual sua idade? '))

print(f'Olá {nome.upper()}! Seja bem vindo (a). Você tem {idade} anos, correto?')














