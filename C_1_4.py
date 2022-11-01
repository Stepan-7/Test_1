while True:
    Num = int(input('Число: '))
    Factorial = 1
    while Num > 1:
        Factorial *= Num
        Num -= 1
    print(Factorial)