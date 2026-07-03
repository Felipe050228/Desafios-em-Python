import re

def validar_formato_cpf(cpf):
    # Regex para o padrão: 000.000.000-00
    padrao = r"^\d{3}\.\d{3}\.\d{3}-\d{2}$"
    
    if re.match(padrao, cpf):
        return True
    return False

# Teste
cpf_teste = "123.456.789-00"
print(f"Formato válido? {validar_formato_cpf(cpf_teste)}")
