Num, Text = 0, 0
while True:
    if Num == 0 and Text == 0:
        Var = input('''
            .______________________________________      
            /                                      \          
            |       (1) Программа с числами        |     
            |       (2) Программа со словами       |     
            \______________________________________/     
                            {''')
        if Var == '1':
            Num += 1
        elif Var == '2':
            Text += 1

####################################################################################################

    if Num == 1 and Text == 0:
        Start = 0
        Max = int(input('''
            .________________________________      
            /                                \          
            |       Количество чисел:        |          
            \________________________________/     
                            {'''))
        X1 = int(input('''
Отсчёт от: 
'''))
        X2 = int(input('''
Отсчёт до: 
'''))
        Interval = int(input('''
Интервал: 
'''))
        for X in range (X1, X2, Interval):
            if Start <= Max:
                print(X)
                Start += 1
        NUM_ = input('''
Хотите закончить?
(1) Да
''')
        if NUM_ == '1':
            Num *= 0
        else:
            Num += 0

####################################################################################################

    elif Num == 0 and Text == 1:
        
        TXT_Start = 0
        TXT_Max = int(input('''
Количество слов: 
'''))
        TXT_1 = ('Привет', 'как', 'твои', 'дела', '?')
        for TXT in TXT_1:
            if TXT_Start <= TXT_Max:
                print(TXT)
                TXT_Start += 1
        TEXT_ = input('''
Хотите закончить?
(1) Да
''')
        if TEXT_ == '1':
            Text *= 0
        else:
            Text += 0