# Aluno: Jordan Julio Francelino da Silva
# Matricula: 20241014050014
print('=-'*100)
print('Identificando um número de Amstrong a partir da análise de um número inteiro!')
n=int(input('Digite um número inteiro: '))

qtd=0  # Quantidade de digitos existentes no número
soma= 0 # Variável responsável pela soma dos digitos

t= n # Variável temporária usada para não interferir no valor original digitado pelo usuário. 
while t > 0: 
    t= t // 10 # Encontrar quantos digitos existem na variável n (quantidade de digitos), 
    qtd  += 1 # após isso soma-se 1 a quantidade
t=n 
while t > 0: 
    digito= t % 10 # Encontrar a posição de cada digito
    potencia=  digito ** qtd  #  A variável potencia será o digito específico elevado a quantidade de digitos, conforme a propriedade de Amstrong
    soma += potencia  # soma de cada um dos digitos elevado a quantidade de digitos
    t= t // 10

if soma == n: # Se o valor da soma for igual ao número, pela propriedade, será considerado um número de Amstrong.
    print(f'O número {n} é um número de Amstrong!')
else:
    print(f'O número {n} NÃO é um número de Amstrong!')