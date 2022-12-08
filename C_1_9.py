print('Пример')
print(sorted([[12, 18, 6, 3], [4, 3, 1, 2], [15, 8, 9, 6]]))
print()

a, b, c = [[44, 18, 24], [102, 1, 3], [4, 2, 3]], [[83, 22, 11], [20, 7, 7], [102, 5, 7]], [[23, 4, 2], [21, 27, 44], [4, 2, 3]]

print('1-е Задание')
print(sorted(a))
print(sorted(a, reverse=True))
print()
print(sorted(b))
print(sorted(b, reverse=True))
print()
print(sorted(c))
print(sorted(c, reverse=True))
print()

print('Задание со звездой (1)')
a1, a2,a3 = sorted(a[0]), sorted(a[1]), sorted(a[2])
ar1, ar2, ar3 = sorted(b[0], reverse=True), sorted(b[1], reverse=True), sorted(b[2], reverse=True)
A = a1, a2, a3
AR = ar1, ar2, ar3
print(sorted(A))
print(sorted(A, reverse=True))
print()

b1, b2, b3 = sorted(b[0]), sorted(b[1]), sorted(b[2])
br1, br2, br3 = sorted(b[0], reverse=True), sorted(b[1], reverse=True), sorted(b[2], reverse=True)
B = b1, b2, b3
BR = br1, br2, br3
print(sorted(B))
print(sorted(B, reverse=True))
print()

c1, c2, c3 = sorted(c[0]), sorted(c[1]), sorted(c[2])
cr1, cr2, cr3 = sorted(c[0], reverse=True), sorted(c[1], reverse=True), sorted(c[2], reverse=True)
C = c1, c2, c3
CR = cr1, cr2, cr3
print(sorted(C))
print(sorted(C, reverse=True))
print()
