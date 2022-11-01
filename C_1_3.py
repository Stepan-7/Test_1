while True:
    Num_1 = int(input('''
    Введите число (Начало отсчёта): 
    '''))
    Num_2 = int(input('''
    Введите число (Конец отсчёта): 
    '''))
    List_1 = []
    List_2 = []
    if Num_1 >= 1:
        for Num in range(Num_1, Num_2):
            for Test in range(2, Num):
                if Num % Test == 0:
                    List_1.append(Num)
                    break
            else:
                List_2.append(Num)
        print(List_1)
        print(List_2)
    else:
        print()