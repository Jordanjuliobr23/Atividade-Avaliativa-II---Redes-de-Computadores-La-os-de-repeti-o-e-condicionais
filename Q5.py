# Aluno: Jordan Julio Francelino da Silva 
# Matricula: 20241014050014 

soma=0 # Variável soma inicianada em 0, responsável por armazenar a soma do valores rotacionados 

n=int(input('Digite um número n, tal que, esse n seja 100 <= n < 10000, obrigatoriamente: '))

num= n # Variável num receberá o número armazenado na variável n, entretanto, ela será rotacionada no laço while enquanto n manterá o valor original 

while 100 <= num < 10000: 
    if num >= 100 and num < 1000: # O uso do If que compreende os números até 3 digitos, ou seja, de 100 a 999
        z= num % 10 # ultimo digito/terceiro
        num= num // 10 # Remove o digito selcionado 
        y= num % 10 # segundo digito torna-se o atual último digito (unidade)
        num= num // 10
        x= num % 10 # o anterior primeiro digito torna-se o segundo digito (dezena)
        num= num // 10
        a1= num # a1 corresponde ao primeiro digito atual (centena)
        a1= z # Agora, o antigo último digito se torna o o primeiro digito
        x1= (a1 * 100) + (x * 10) + (y*1)  # soma dos digitos rotacionados, quando n tem apenas 3 digitos 
        soma= a1 + x + y # Se o número solicitado pelo usuário obedecer o intervalo presente no if, a variável soma irá armazenar apenas a soma dos digitos rotacionados, em um número de 3 digitos.
    elif num >= 1000 and num < 10000: # O uso do Elif compreende os números a partir de 4 digitos, ou seja, de 1000 a 9999
        z= num % 10 # Antigo Quarto digito (Unidade)
        num= num // 10 # remoção do digito selecionado
        y= num % 10 # Terceiro digito (Dezena)
        num= num // 10 
        x= num % 10  # Segundo digito (Centena)
        num= num // 10 # 
        w= num % 10  # Primeiro digito (Milhar)
        num= num // 10 
        a2= num # A variável a2 torna-se a responsável pelo primeiro número atual
        a2 = z # O antigo último número torna-se o primeiro
        x1= (a2 * 1000) +  (w * 100) + (x * 10) + y # soma dos digitos rotacionados, quando n tem 4 digitos 
        soma= a2 + w + x + y # Se o número solicitado pelo usuário obedecer o intervalo presente no if, a variável soma irá armazenar apenas a soma dos digitos rotocionados, em um número de 4 digitos.
print(f'O valor rotacionado do número {n} será {x1}') 
print(f'A soma dos valores rotacionados presentes em {x1} corresponde a: {soma} ')
  
