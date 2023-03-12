def grayCode(n):
    lst = [0]
    if n== 0:
        return lst
    lst.append(1)
    cur = 1
    for i in range(2,n+1):
        cur *= 2
        for j in range(len(lst)-1,-1,-1):
            lst.append(cur+lst[j])
    return lst
n = int(input())
print(*(grayCode(n)))