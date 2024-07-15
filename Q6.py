# Aluno: Jordan Júlio Francelino da Silva
# Matricula: 20241014050014 
print(f'Os números maiores que 1 e menores que 100000, múltiplos de 2 ou 5, que podem ser obtidos pela soma de potências de 5 dos seus dígitos são: ')
num=0 

for num in range(2, 100000) : # Laço que contempla os números maiores que 1 até 100000
    if num % 2 == 0 or num % 5 == 0: # Se forem mútiplos de 5 ou 2, realize a condição abaixo
        n= num # variável n sofrerá as alterções do laço
        z= n % 10 # Quinto digito 
        n= n // 10 # remove o digito selecionado
        y= n % 10 # Quarto digito 
        n= n // 10 
        x= n % 10 # Terceiro digito 
        n= n // 10
        w= n % 10  # Quarto digito 
        n= n // 10
        v= n % 10 # Quinto digito 
        soma= (z**5) + (y**5) + (x**5) + (w**5) + (v**5) # A soma das potências de 5 de cada digito 
        if num == soma: # Caso a soma for igual ao número, mostre-o
            print(num)

