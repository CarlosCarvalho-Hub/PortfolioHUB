#Exercício 1
print("Exercício 1")
numero_1 = float(input("Digite o primeiro número: "))
numero_2 = float(input("Digite o segundo número: "))
print("+  (adição)")
print("-  (subtração)")
print("*  (multiplicação)")
print("/  (divisão)")
op = input("Digite a operação desejada: ")
if op == "+":
    resultado = numero_1 + numero_2
    print("Resultado:", resultado)
elif op == "-":
    resultado = numero_1 - numero_2
    print("Resultado:", resultado)
elif op == "*":
    resultado = numero_1 * numero_2
    print("Resultado:", resultado)
elif op == "/":
    if numero_2 != 0:
        resultado = numero_1 / numero_2
        print("Resultado:", resultado)
    else:
        print("Erro: divisão por zero!")
else:
     print("Operação inválida!")

#Exercício 2
print("Exercício 2")
quantidade = 0
soma = 0
maiores_que_20 = 0
while True:
    valor = float(input("Digite um valor (0 para parar): "))
    if valor == 0:
        break
    quantidade += 1
    soma += valor
    if valor > 20:
        maiores_que_20 += 1
if quantidade > 0:
    media = soma / quantidade
else:
    media = 0
print("Quantidade de valores:", quantidade)
print("Soma:", soma)
print("Média:", media)
print("Valores maiores que 20:", maiores_que_20)

#Exercício 3
print("Exercício 3")
total = 0
aprovados = 0
reprovados = 0
soma = 0
while True:
    nota = float(input("Digite a nota do aluno (-1 para parar): "))
    if nota == -1:
        break
    total += 1
    soma += nota
    if nota >= 5:
        aprovados += 1
    else:
        reprovados += 1
if total > 0:
    media = soma / total
else:
    media = 0
print("Total de alunos que fizeram a prova:", total)
print("Aprovados:", aprovados)
print("Reprovados:", reprovados)
print("Média da turma:", media)

#Exericício 4
print("Exericício 4")
soma_total = 0
quantidade_total = 0
soma_pares = 0
quantidade_pares = 0
soma_impares = 0
quantidade_impares = 0
while True:
    num = int(input("Digite um número (0 para sair): "))
    if num == 0:
        break
    soma_total += num
    quantidade_total += 1
    if num % 2 == 0:
        soma_pares += num
        quantidade_pares += 1
    else:
        soma_impares += num
        quantidade_impares += 1
media_pares = soma_pares / quantidade_pares\
    if quantidade_pares > 0 \
    else 0
media_impares = soma_impares / quantidade_impares \
    if quantidade_impares > 0 \
    else 0
print("Quantidade total de números:", quantidade_total)
print("Soma total:", soma_total)
print("Média dos pares:", media_pares)
print("Média dos ímpares:", media_impares)