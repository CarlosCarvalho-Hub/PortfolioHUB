#Exercício 1
Raio = float(input("Digite o valor do raio de uma esfera para calcular o volume da uma esfera: "))
Volume = (4/3) * 3.14 * (Raio ** 3)
print("O volume da esfera é", Volume,"cm³")

#Exercício 2
Massa = float(input("Digite seu peso corporal em kg para calcular a massa de água necessária para consumo: "))
Agua = Massa * 0.03
print("A dose ideal necessária de água por dia é:", Agua, "litros")

#Exercício 3
import math
print("Para calcular a distância entre os seguintes pontos no plano cartesiano, digite o valor de suas coordenadas")
x1 = float(input("Digite x1: "))
y1 = float(input("Digite y1: "))
x2 = float(input("Digite x2: "))
y2 = float(input("Digite y2: "))
Distancia = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)
print("A distância entre os pontos no plano cartesiano é:", Distancia)

#Exercício 4
print("Digite dois valores inteiros quaisquer para serem classificados em ordem crescente")
Numero1 = int(input("Digite o primeiro número: "))
Numero2 = int(input("Digite o segundo número: "))
if Numero1 < Numero2:
    print("Ordem crescente:", Numero1," ,",Numero2)
else:
    print("Ordem crescente:", Numero2,",",Numero1)