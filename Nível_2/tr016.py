lista_de_menor = []
lista_de_maior = []
pessoas = {}
while True:
    while True:
        try:
            pessoas['nome'] = input('\033[1;32mdigiti seu nome: ').strip().capitalize()
            while True:
                try:
                    pessoas['idade'] = int(input(f'\033[1;32mdigiti sua idade: '))
                    print('\033[m')
                except:
                    print('\033[1;31mDIGITI UM VALOR VALIDO')
                    print('\033[m')
                else:
                    break
        except:
            print('\033[1;31mDIGITI UM VALOR VALIDO')
            print('\033[m')
        else:
            if pessoas['idade'] >= 18:
                lista_de_maior.append(pessoas.copy())
            else:
                lista_de_menor.append(pessoas.copy())
            while True :
                sim_nao = input('\033[1;32mvocé quer continuar: ').strip().upper()[0]
                print('\033[m') 
                if sim_nao == 'N':
                    break
                elif sim_nao == 'S':
                    break
                else:
                    print('\033[1;31mDIGITI UM VALOR VALIDO')
                    print('\033[m') 
        if sim_nao == 'N':
            break
        elif sim_nao == 'S':
            ''
    if sim_nao == 'N':
        break
    elif sim_nao == 'S':
        ''
print('\033[1;34mmaiores de idade')
for i in lista_de_maior:
    print(f'\033[1;34m{i}\033[m')            
        