n=int(input())
factorial = 1
while n>1 and n<100:
    factorial*=n
    n-=1
    print(factorial)