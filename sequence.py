def seq(n):
    if n <=1:
        return 1
    elif n == 2:
        return 2
    return seq(n-1)+seq(n-2)+seq(n-3)+n
n = int(input())
print(seq(n))