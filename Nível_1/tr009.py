sim_ou_não = None
palindromo = str(input('varifique se e um palíndromo; ')).lower().strip()
invert_palavra = palindromo[::-1]
print(palindromo)
print(invert_palavra)
if palindromo == invert_palavra:
    sim_ou_não = True
else:
    sim_ou_não = False
print(sim_ou_não)
