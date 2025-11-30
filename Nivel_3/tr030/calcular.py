import operadores
while True:
    try:
        num1 = int(input("\033[1;32mdigiti um numero: "))
        operador = input("vocé quer [+,-,*,/] ")
        num2 = int(input("digiti outro numero: "))
    except:
        print("\033[m\033[1;31mERRO POR FAVOR TENTE DE NOVO\033[m\033[1;32m")
    else:
        if operador == "+":
            operadores.adiçao(primeiro_num=num1,segundo_num=num2)
        elif operador == "-":
            operadores.subitraçao(primeiro_num=num1,segundo_num=num2)
        elif operador == "*":
            operadores.mutiplicaçao(primeiro_num=num1,segundo_num=num2)
        elif operador == "/":
            operadores.divisao(primeiro_num=num1,segundo_num=num2)
        else: 
            print("\033[m\033[1;31mERRO OPERADOR NÃO RECONHECIDO POR FAVOR TENTE DE NOVO\033[m\033[1;32m")
        while True:
            try:
                continuar = input("quer continuar [S|N]:").upper().strip()[0]
            except:
                print("\033[m\033[1;31mERRO POR FAVOR TENTE DE NOVO\033[m\033[1;32m")
            else:
                if continuar == "N" or continuar == "S":
                    break
                else:
                    print("\033[m\033[1;31mERRO POR FAVOR TENTE DE NOVO\033[m\033[1;32m")
        if continuar == "N":
            break