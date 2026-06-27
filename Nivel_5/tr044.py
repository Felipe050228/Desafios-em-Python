num1 = 10
num2 = 10

try:
    resultado = num1 / num2
    print(f"O resultado é: {resultado}")
except ZeroDivisionError:
    print("Erro: Não é possível realizar uma divisão por zero.")
