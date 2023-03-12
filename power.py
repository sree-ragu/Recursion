def pow(n,k,d):
    if n==1 or k == 0:
        return 1%d
    elif k == 1:
        return n%d
    
    if k%2 == 1:
        return n%d *pow(n,k-1,d)
    else:
        res = pow(n,k//2,d)
        return ((res%d)*(res%d))%d
n,k,d = map(int,input().split())
print(pow(n,k,d))