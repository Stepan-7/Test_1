num = int(input('Введите число:'))
if num<=1000:
    for x in range(11):
        print(f'{num} в степени {x} = {num**x}')
else:
    print('!Число слишком большое!')