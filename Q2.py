# Aluno: Jordan Julio Francelino da Silva
# Matricula: 20241014050014

print('=-'*100)
print('Quantos números de exatos 9 digitos existem, NÃO possuindo tres digitos consecutivos e cuja sua soma seja maior que 8?')

c=0 # Criação de uma variável responsável por contar os números de 9 digitos que correspondem a essas condições.
for n in range (100000000, 1000000000): # Laço de repetição que compreende todos os números de 9 digitos 
    num = n # Criação da variável num para ser processada pelo programa.
    x9= num % 10 # Nono digito
    num = num // 10 # processo realizado para retornar ao digito anterior;
    x8= num % 10 #  Oitavo digito
    num = num // 10 # retorno ao digito anterior 
    x7= num % 10 #  Sétimo digito 
    num= num // 10 
    x6= num % 10 # Sexto digito
    num= num // 10 
    x5= num % 10 # Quinto digito
    num = num // 10
    x4= num % 10 # Quarto digito
    num= num // 10 
    x3= num % 10 # Terceiro digito
    num= num // 10
    x2= num % 10 # Segundo digito
    num= num // 10
    x1= num % 10 # Primeiro
    num= num // 10
    if x9 + x8 + x7 < 8: # se a soma dos tres digitos forem menores que 8, eles serão acrescentados na contagem.
        c= c + 1 
    elif x8 + x7 + x6 < 8: 
        c= c + 1 
    elif x7 + x6 + x5 < 8:
        c= c + 1
    elif x6 + x5 + x4 < 8:
        c= c + 1
    elif x5 + x4 + x3 < 8 :
        c= c + 1
    elif x4 + x3 + x2 < 8:
        c= c + 1
    elif x3 + x2 + x1 < 8: 
        c= c + 1 
    if n % 1000000 == 0:
        print (n)
print(f'A quantidade de números com nove digitos que atendem a essas tres condições são: {c}')

