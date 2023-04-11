# Q1

n1=5
n2=8
if(n1<n2):
    print(n2)

# Q2
idade=int(input('digite sua idade: '))
if(idade<=17):
    print('menor de idade')
else:
    print('maior de idade')

# Q3

nm=input('Nome: ')
idade=int(input('Idade: '))
if(idade>18):
    print(f'{nm}, você pode dirigir')
else:
    print(f'{nm}, você não pode dirigir')

# Q4

n1=int(input('digite um numero: '))
n2=int(input('digite um numero: '))
n3=int(input('digite um numero: '))
n4=int(input('digite um numero: '))
soma=(n1+n2+n3+n4)/4
if(soma>=7):
    print('você passou')
else:
    print('não passou')

# Q5

n1=9
if(n1%2==0):
    print('par')
else:
    print('impar')

# Q6

aumento=1.1
salario_f=float(input('digite seu salario: '))
if(salario_f>1500):
    novo_salario=salario_f*aumento
    print(f'você recebeu um aumento de 10%, novo salário:{novo_salario}')
else:
    print('sem aumento disponível.')

# Q7

numeros=[5,6,7,1,2]
maior=numeros[0]
menor=numeros[0]
for num in numeros:
    if num >maior:
        maior=num
    if num<menor:
        menor=num

        menor=num
print(f'maior valor é: {maior}')
print(f'menor valor: {menor}')

# Q8
string=input('digite uma palavra: ')
string_invertida=string[::-1]
if string == string_invertida:
    print('é um palindromo')
else:
    print('não é um palindromo')