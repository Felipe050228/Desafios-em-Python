numlist = []
try:
    for i in range(0,10):
        while True:
            try:
                num = int(input(f'\033[1;32m{i+1}º digiti um numero: '))
            except: 
                print('\033[1;31mPORFAVOR DIGITI UM VALOR VALIDO \033[m')
                numlist.pop   
            else:
                numlist.append(num)
                break   
except:
    print('\033[1;31mPORFAVOR DIGITI UM VALOR VALIDO \033[m')
    numlist.pop
    print(numlist)
else:
    print(f'\033[m\033[1;34m{numlist}\033[m')
    print(f'\033[1;33m o maior numero da lista e {max(numlist)}\033[m')
