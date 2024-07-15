# Aluno: Jordan Julio Francelino da Silva
# Matricula: 20241014050014


print('=-'*100)
print('Sistema de Análise de números digitados')
print('Caso desejar encerrar o programa digite 0!')

qtd=0 # Quantidade de números digitados pelo usuário

maior=0 #  Variável responsável por atribuir o valor n como o maior, se caso aparecer um valor maior que o anterior, esse novo valor será atribuido a variável "maior".

menor=1000000000000000000 # variável responsável por atribuir o valor n como o menor, foi atribuido "1000000000000000000" pois por ser um valor muito alto, qualquer valor menor a esse mesmo se for o primeiro valor será atribuido a variável "menor". Portanto, caso aparecer um valor menor que o anterior, esse valor será atribuido a variável menor.

# soma os valores digitados pelo usuário antes dele digitar 0.
soma= 0 
#  a média entre a soma dos valores digitados antes dele digitar 0 e a quantidade de valores digitados.
media=0
n=1 
while n != 0: 
    n=int(input('Digite um número inteiro: '))
    qtd= qtd + 1 # adiciona-se 1 a variável qtd, 
    soma= soma + n # Adiciona-se o número a soma
    if n >= maior:
        maior= n # Se 'n' conter um valor maior do que está armazenado em 'maior', 'maior' recebe 'n'
    if n < menor and n > 0: # Se 'n' conter um valor menor do que está armazendo em 'menor', 'menor' recebe 'n'
        menor = n 
    # Se o usuário digitar o número 0, o laço será interrompido e o programa será encerrado
    if n == 0: 
        break 
    # Média da soma de todos os valores digitados pela quantidade de valores digitados 
    media= soma/qtd
print('=-'*50)
print(f'Analisando...')
print(f'O menor número digitado foi {menor}')
print(f'O maior número digitado foi {maior}')
print(f'A média dos valores digitados foi {media}')