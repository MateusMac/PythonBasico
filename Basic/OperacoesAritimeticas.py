# Solicita que o usuário insira um número
num1 = input("Insira o primeiro número: ")
# Solicita que o usuário insira um segundo número
num2 = input("Insira o segundo número: ")

# Realiza a soma entre dois valores
sum = float(num1) + float(num2)
# Realiza a subtração entre dois valores
sub = float(num1) - float(num2)
# Realiza a multiplicação entre dois valores
mul = float(num1) * float(num2)
# Realiza a divisão entre dois valores
div = float(num1) / float(num2)

print("A soma dos números {0} e {1} é {2}".format(num1, num2, sum))
print("A subtração dos números {0} e {1} é {2}".format(num1, num2, sub))
print("A multiplicação dos números {0} e {1} é {2}".format(num1, num2, mul))
print("A divisão dos números {0} e {1} é {2}".format(num1, num2, div))
