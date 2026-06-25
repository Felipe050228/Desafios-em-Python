from contextlib import contextmanager

@contextmanager
def abrir_arquivo(caminho, modo):
    arquivo = open(caminho, modo)
    try:
        yield arquivo
    finally:
        arquivo.close()

# Como usar:
with abrir_arquivo('exemplo.txt', 'w') as f:
    f.write('bct  Olá, mundo!')
