import logging

# 1. Configurar o logger
logger = logging.getLogger('MeuLoggerDeErros')
logger.setLevel(logging.ERROR) # Grava apenas nível ERROR ou CRITICAL

# 2. Criar o manipulador para salvar em arquivo
arquivo_handler = logging.FileHandler('erros.log')
arquivo_handler.setLevel(logging.ERROR)

# 3. Definir o formato da mensagem: Data - Hora - Nível - Mensagem
formato = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s', datefmt='%d/%m/%Y %H:%M:%S')
arquivo_handler.setFormatter(formato)

# 4. Adicionar o manipulador ao logger
logger.addHandler(arquivo_handler)

# 5. Exemplo de uso em um bloco try/except
try:
    resultado = 10 / 0
except ZeroDivisionError as e:
    logger.error("Ocorreu um erro ao tentar dividir um número por zero.", exc_info=True)

print("Erro registrado com sucesso no arquivo 'erros.log'.")
