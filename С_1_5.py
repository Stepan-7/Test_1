while True:
    start = int(input('''
Отсчёт от_:   '''))
    end = int(input('''
Отсчёт до_:   '''))
    if end - start < 2:
        print('''
Диапазон чисел меньше 2''')
    elif end - start <= 19999999:
        list = []
        num = 0
        num_y = 0
        list_y = []
        for mass in range(start, end+1):
            list.append (mass)
            Len = len(list)


        for x in range(0, Len):
            if list[x] % 3 == 0:
                num += 1

        for y in range(start,Len):
            if list [y] % 2 == 1:
                num_y += 1
                list_y.append (y)
        s = (sum(list_y)) / num_y

        print('''
    Лист чисел_:  ''' + str(list))
        print('''
    Лист Чётных чисел_:   ''' + str(list_y))
        print('''
    Числа, делящиеся на 3_:   ''' + str(num))
        print('''
    Ср/ар. Чётных чисел_:   ''' + str(s))
    else:
        print('''
Диапазон чисел слишком большой или начальное число больше конечного. Введите другие числа.''')