Str=['']
Del = []
def Input(I):
    while I != 0:
        B = int(input('позиция  '))
        C = str(input('слово  '))
        Str.insert(B, C)
        I *= 0
    
def Delete(D):
    while D != 0 :
        G = input('позиция  ')
        del Str[G]
        D *= 0

while True:
    A = input(f'''
{Str}
1 = вставить
2 = удалить
''')
    if A == '1':
        Input(1)
    elif A == '2':
        Delete(1)

