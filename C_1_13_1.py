def CheckLeap(Year):
    if ((Year%400==0)or(Year%100!=0)and(Year%4==0)):
        print('Високосный год ')
    else:
        print('Невесокосный год ')

Year = int(input('Введите год'))
CheckLeap(Year)