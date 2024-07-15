# Aluno: Jordan Julio Francelino da Silva
# Matricula: 20241014050014
print('=-'*100)
print('Qual o maior número decrescente entre 1000000 e 2000000? ')
# 1- Variável responnsável por armaar aquele que será o maior número decrescente do intervalo
maior=0 
# 2- Laço de repetição "for" que irá contemplar todos os números do intervalo
for n in range (1000000,2000000): 
    num = n 
    n7= n % 10 # Sétimo número
    n= n // 10 # A variável n agora terá seu último digito removido
    n6= n % 10 # Sexto número 
    n= n // 10 
    n5= n % 10 # Quinto número 
    n= n // 10 
    n4= n % 10 # Quarto número
    n= n // 10
    n3= n % 10 # Terceiro número
    n= n // 10
    n2= n % 10 # Segundo número
    n= n // 10 
    n1= n % 10 # Primeiro número
    if n1 >= n2 and n2 >= n3 and n3 >= n4 and n4 >= n5 and n5 >=  n6 and n6 >= n7 : # Condição para verificar se o número é decrescente
        if num > maior: 
            maior = num   # Se o número for maior que o valor atribuido a variável 'maior', adiciona esse valor a 'maior'. 
print(f'O maior número decrescente entre 1000000 e 2000000 é: {maior}')
        