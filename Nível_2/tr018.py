A = 0
E = 0
I = 0
O = 0
U = 0
frazes = str(input('\033[1;32mdigiti uma frase : ')).strip().upper()
A = frazes.count('A')
E = frazes.count('E')
I = frazes.count('I')
O = frazes.count('O')
U = frazes.count('U')
print(f'\033[m\033[1;34mtemos \n {A}:A \n {E}:E \n {I}:I \n {O}:O \n {U}:U')