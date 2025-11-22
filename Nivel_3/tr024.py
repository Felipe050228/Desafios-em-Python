def texto (nome_texto , texto_escrito):
    with open (nome_texto, 'w', encoding='utf-8') as arquivo:
        arquivo.write(texto_escrito)
        print(f'texto escrito no arquivo {nome_texto} com sucesso.')

    print(f'lendo o texto do arquivo {nome_texto}')

    with open(nome_texto,'r',encoding = 'utf-8') as arquivo:
        texto_lido = arquivo.read()
        print(texto_lido)



escreva_um_texto = input('digiti um texto: ')
de_nome_ao_texto = input('agora de um nome ao texto: ')
texto(nome_texto=de_nome_ao_texto,texto_escrito=escreva_um_texto)