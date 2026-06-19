def numeros_pares_infinitos():
    numero = 0
    while True:
        yield numero
        numero += 2

# Exemplo de uso para imprimir os 10 primeiros números pares
gerador = numeros_pares_infinitos()
for _ in range(100):
    print(next(gerador))
