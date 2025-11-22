def convert_Celsi_Fahre(graus=0):
    converte_Fahrenheit = (graus*9/5)+32
    print(f'{graus} graus Celsius em Fahrenheit fica {converte_Fahrenheit}')

temperatura = int(input('digiti uma temperatura para converte em Fahrenheit.: '))
convert_Celsi_Fahre(graus=temperatura)