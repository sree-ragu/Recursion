def reverse(s,i):
    if i == 1:
        return s[0]
    
    return s[i-1]+reverse(s,i-1)
s = input().strip()
print(reverse(s,len(s)))