numeros = list(range(1, 51))

# Filtrando números primos utilizando compreensão de listas
primos = [n for n in numeros if n > 1 and all(n % i != 0 for i in range(2, int(n**0.5) + 1))]

print(primos)
# Saída: [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47]
