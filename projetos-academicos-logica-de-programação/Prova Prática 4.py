#Exercicio 1
print("Exercicio 1")
valor_final = int(input("Digite o valor final de uma sequência de números: "))
contador = 0
for i in range(1, valor_final + 1):
    print(i)
    contador += 1
print("A quantidade de valores gerados foi:", contador)

#Exercicio 2
print("Exercicio 2")
valor_inicial = int(input("Digite o valor inicial de uma sequência de números: "))
contador = 0
for i in range(valor_inicial, -1, -1):
    print(i)
    contador += 1
print("Quantidade de valores gerados foi:", contador)

#Exercicio 3
print("Exercicio 3")
soma = 0
for i in range(1, 501):
    soma += i
print("A soma do número 1 ao 500 é:", soma)

#Exercicio 4
print("Exercicio 4")
soma = 0
for i in range(1, 501):
    if i % 2 != 0 and i % 3 == 0:
        soma += i
print("A soma dos números ímpares e múltiplos de 3 do 1 ao 500 é:", soma)

#Exercicio 5
print("Exercicio 5")
for i in range(7):
    for j in range(7):
        print(i, "-", j)

#Exercicio 6
print("Exercicio 6")
for i in range(7):
    for j in range(i, 7):
        print(i, "-", j)