import os
import shutil

""""Organiza arquivos em pastas por extensão
 Como usar:Abra um editor de texto (como Bloco de Notas, VS Code ou Notepad++).Copie e cole o código acima.Altere CAMINHO_PARA_A_SUA_PASTA pelo diretório real que deseja organizar (lembre-se de manter o r antes das aspas no Windows).Salve o arquivo com o nome organizador.py.Abra o terminal ou prompt de comando e execute o script digitando: python organizador.py Certifique-se de que o Python esteja instalado e configurado corretamente no seu sistema. O script irá criar pastas para cada tipo de arquivo (baseado na extensão) e mover os arquivos para as pastas correspondentes. """

# Defina aqui o caminho da pasta que você quer organizar
# Exemplo no Windows: "C:\\Users\\SeuUsuario\\Downloads"
# Exemplo no Linux/Mac: "/home/SeuUsuario/Downloads"
caminho_pasta = r"CAMINHO_PARA_A_SUA_PASTA"

# Altera o diretório de trabalho atual para a pasta escolhida
os.chdir(caminho_pasta)

# Lista todos os arquivos na pasta
for arquivo in os.listdir():
    # Ignora diretórios (pastas) e mantém apenas arquivos
    if os.path.isdir(arquivo):
        continue

    # Separa o nome do arquivo e sua extensão (ex: 'documento', '.pdf')
    nome, extensao = os.path.splitext(arquivo)

    # Verifica se o arquivo tem extensão (evita erros com arquivos sem extensão)
    if extensao:
        # Remove o ponto da extensão para usar como nome da pasta (ex: 'pdf')
        nome_pasta = extensao[1:].lower()

        # Cria a pasta da extensão se ela não existir
        if not os.path.exists(nome_pasta):
            os.makedirs(nome_pasta)

        # Move o arquivo para a pasta correspondente
        shutil.move(arquivo, os.path.join(nome_pasta, arquivo))

print("Arquivos organizados com sucesso!")
