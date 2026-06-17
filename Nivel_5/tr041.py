import time
from functools import wraps

def medir_tempo(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        inicio = time.perf_counter()
        resultado = func(*args, **kwargs)
        fim = time.perf_counter()
        tempo_total = fim - inicio
        print(f"A função '{func.__name__}' levou {tempo_total:.4f} segundos para executar.")
        return resultado
    return wrapper

# Exemplo de uso:
@medir_tempo
def processar_dados(n):
    return sum(i * i for i in range(n))

processar_dados(1000000)
