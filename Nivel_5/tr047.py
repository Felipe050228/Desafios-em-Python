import requests

# Substitua pela URL dos dados que deseja baixar
url = "https://cdn.wsform.com/wp-content/uploads/2020/06/color_srgb.csv"
nome_arquivo = "dados_baixados.csv"

# Realiza a requisição
response = requests.get(url)

# Verifica se a requisição foi bem-sucedida (status 200)
if response.status_code == 200:
    # Salva o conteúdo em um arquivo local
    with open(nome_arquivo, "wb") as arquivo:
        arquivo.write(response.content)
    print(f"Dados baixados e salvos com sucesso em {nome_arquivo}")
else:
    print(f"Erro ao acessar a URL. Status: {response.status_code}")
