import re

regex = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
email = "exemplo@dominio.com"

if re.match(regex, email):
    print("E-mail válido")
else:
    print("E-mail inválido")
