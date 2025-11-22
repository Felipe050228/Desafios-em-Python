num1 = 0 
num2 = 1
while True:
    num3 = num1 + num2
    resuta = num3 + num2
    num1 = resuta - num3
    num2 = num3
    print(num3 ,end=',')
    if num3 == 55:
        break