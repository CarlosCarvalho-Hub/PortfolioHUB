#Exercício 1
print("Exercício 1:")
soma_pares = 0
quantidade_pares = 0
soma_impares = 0
quantidade_impares = 0
total_numeros = 0
soma_total = 0
while True:
    numero = int(input("Digite um número (0 para sair): "))
    if numero == 0:
        break
    total_numeros += 1
    soma_total += numero
    if numero % 2 == 0:
        soma_pares += numero
        quantidade_pares += 1
    else:
        soma_impares += numero
        quantidade_impares += 1
media_pares = soma_pares / quantidade_pares \
    if quantidade_pares > 0 \
    else 0
media_impares = soma_impares / quantidade_impares \
    if quantidade_impares > 0 \
    else 0
print("Quantidade total:", total_numeros)
print("Soma total:", soma_total)
print("Média dos pares:", media_pares)
print("Média dos ímpares:", media_impares)
#Exercício 2
print("Exercício 2")
quantidade_de_valores = 0
soma_de_valores = 0
maior_valor = None
menor_valor = None
quantidade_maior_que_50 = 0
while True:
    valor = float(input("Digite um valor (0 para sair): "))
    if valor == 0:
        break
    quantidade_de_valores += 1
    soma_de_valores += valor
    if (maior_valor
            is None or valor > maior_valor):
        maior_valor = valor
    if (menor_valor
            is None or valor < menor_valor):
        menor_valor = valor
    if valor >= 50:
        quantidade_maior_que_50 += 1
media_de_valores = soma_de_valores / quantidade_de_valores \
    if quantidade_de_valores > 0 \
    else 0
print("A quantidade de valores digitados é:", quantidade_de_valores)
print("A Soma de valores digitados é:", soma_de_valores)
print("A média de valores digitados é:", media_de_valores)
print("O maior valor digigitado é:", maior_valor)
print("O menor valor digitado é:", menor_valor)
print("O(s) valores maiores que 50 são:", quantidade_maior_que_50)
#Exercício 3
print("Exercício 3")
candidato_1 = candidato_2 = candidato_3 = 0
votos_nulos = votos_brancos = 0
total_de_votos = 0
while True:
    voto = int(input("Vote (1,2,3,5=nulo,6=branco, 0=sair): "))
    if voto == 0:
        break
    total_de_votos += 1
    if voto == 1:
        candidato_1 += 1
    elif voto == 2:
        candidato_2 += 1
    elif voto == 3:
        candidato_3 += 1
    elif voto == 5:
        votos_nulos += 1
    elif voto == 6:
        votos_brancos += 1
percentual_de_votos_nulos = (votos_nulos / total_de_votos * 100) \
    if total_de_votos > 0 \
    else 0
percentual_de_votos_brancos = (votos_brancos / total_de_votos * 100) \
    if total_de_votos > 0 \
    else 0
print("O candidato 1 teve:", candidato_1, "votos")
print("O candidato 2 teve:", candidato_2, "votos")
print("O candidato 3 teve:", candidato_3, "votos")
print("A quantidade de votos nulos foi:", votos_nulos)
print("A quantidade de votos brancos foi:", votos_brancos)
print("O percentual de votos nulos é:", percentual_de_votos_nulos, "%")
print("O percentual de votos brancos é:", percentual_de_votos_brancos, "%")
#Exercício 4
print("Exercício 4")
salario_minimo = float(input("Digite o valor do salário mínimo: "))
menos_5 = 0
entre_5_10 = 0
mais_10 = 0
folha_total = 0
while True:
    salario = float(input("Digite o salário (0 para sair): "))
    if salario == 0:
        break
    folha_total += salario
    if salario < 5 * salario_minimo:
        menos_5 += 1
    elif salario < 10 * salario_minimo:
        entre_5_10 += 1
    else:
        mais_10 += 1
print("",menos_5, "funcionarios ganham menos de 5 salários mínimos:")
print("",entre_5_10,"funcionarios ganham entre 5 a 10 salários mínimos:")
print("",mais_10,"funcionarios ganham 10 ou mais salários mínimos:")
print("A folha total da empresa é:", folha_total,"R$")