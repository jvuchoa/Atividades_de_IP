palavra = input("Digite uma palavra: ")

# Invertendo a palavra utilizando um loop for
palavra_invertida = ""
for letra in palavra:
    palavra_invertida = letra + palavra_invertida

# Verificando se a palavra original e a invertida são iguais
if palavra == palavra_invertida:
    print("A palavra é um palíndromo!")
else:
    print("A palavra não é um palíndromo.")


