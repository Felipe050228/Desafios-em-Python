import math
def fatorial(num_inici=0):
    resu_fato = []
    resutado = 1
    if num_inici < 0:
        print('Não existe fatorial para números negativos')
    else:
        for i in range(num_inici,0,-1):
            resu_fato.append(num_inici)
            print(i,end=' ')
            num_inici -= 1
    total = math.prod(resu_fato)
    print(f'={total}')
print('calcular o fatorial')
fatorial(num_inici=10)