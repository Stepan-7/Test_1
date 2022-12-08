List = []
List_R = []
Range = int(input('Промежуток:  '))
for Num in range(1, 101):
    List.append(Num)
print(List)
print(List[::-1])

for Num_Range in range(1, 101, Range):
    List_R.append(Num_Range)
print(List_R)