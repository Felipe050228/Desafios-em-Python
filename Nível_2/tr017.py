lista_compras = []
cont_mais = 1
cont_mais_remove = 1
while True:
    if cont_mais < 2 :
        compra = input('\033[1;32mdeseja compra alguma coisa?:\033[m \033[1;31m[digiti ¨sair¨ para parar]\033[m\033[1;32m ')
    elif cont_mais >= 2 :
        compra = input('\033[1;32mdeseja compra mais alguma coisa?:\033[m \033[1;31m[digiti ¨sair¨ para parar]\033[m\033[1;32m ')
    if compra == 'sair':
        break
    else :
        lista_compras.append(compra) 
        cont_mais += 1
while True:
    try :
        if cont_mais_remove < 2:
            remover_compra = input('\033[1;32mdeseja remover alguma coisa?:\033[m \033[1;31m[digiti ¨sair¨ para parar]\033[m\033[1;32m ')
        elif cont_mais_remove >= 2:
            remover_compra = input('\033[1;32mdeseja remover mais alguma coisa?:\033[m \033[1;31m[digiti ¨sair¨ para parar]\033[m\033[1;32m ')
        if remover_compra == 'sair':
            break
        else:
            lista_compras.remove(remover_compra)
            cont_mais_remove += 1
    except:
        print('\033[1;31mPOR FAVOR DIGITI UM OBJETO QUE ESTEJA NA LISTA\033[m')
print('\033[1;34mLISTA DE COMPRAS')
for i in lista_compras:
    print(f'\033[1;34m  {i}\033[m')