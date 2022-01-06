# Importa o modulo de números complexos
import cmath

a = float(input("Insira a: "))
b = float(input("Insira b: "))
c = float(input("Insira c: "))

# Calcula o discriminante
d = (b ** 2) - (4 * a * c)

# Encontra as duas soluções
sol1 = -b - cmath.sqrt(d) / (2 * a)
sol2 = -b + cmath.sqrt(d) / (2 * a)

print("As soluções são {0} e {1}".format(sol1, sol2))
