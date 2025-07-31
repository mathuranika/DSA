t = int(input())

while t > 0:
    n = int(input())
    s = str(input())
    res = 0
    for i in range(0,n-1):
        if s[i]==s[i+1]:
            res+=1
    print(res)
    t-=1
