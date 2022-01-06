P = int(input("Por favor, insira um valor para P: "))
Q = int(input("Por favor, insira um valor para Q: "))

# Método 1
# Usaremos o método mais "bruto" possível, usando uma variável temporária
temp = P
P = Q
Q = temp

print("Valor de P após a troca: ", P)
print("Valor de Q após a troca: ", Q)

# Método 2
# Usando o operador virgula
P, Q = Q, P

# Método 3
# Usando o método XOR
P = P ^ Q
Q = P ^ Q
P = P ^ Q
