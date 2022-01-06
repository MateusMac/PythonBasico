# Solicita que o usuário insira três lados de um triangulo
a = float(input("Insira o primeiro lado: "))
b = float(input("Insira o segundo lado: "))
c = float(input("Insira o terceiro lado: "))

# Calcula o semi-perimetro
s = (a + b + 2) / 2

# Calcula a area
area = (s * (s - a) * (s - b) * (s - c)) ** 0.5

print("A área do triangulo é %0.2f" % area)
