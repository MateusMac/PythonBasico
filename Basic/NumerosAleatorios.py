# Importação da biblioteca random
import random

# Gera um número aleatório, float ou int
n = random.random()
print(n)

# Gera um int aleatório dentro de um range
n = random.randint(0, 50)
print(n)

# Gera uma lista aleatório com um número máximo de 6 posições num range de 0 a 50
list = random.sample(range(0, 50), 6)
print(list)
