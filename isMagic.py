def sum(n):
    if n<=9:
        return n
    return n%10 + sum(n//10)
n = int(input())
while(n>9):
    n = sum(n)
print('YES' if n == 1 else 'NO' )