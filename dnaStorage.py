t = int(input())

while t > 0:
    n = int(input())
    s = input()
    s = str(s)
    i = 0
    res = ""
    alph = {"00":"A","01":"T","10":"C","11":"G"}
    while i<(n-1):
        res+= alph[s[i:i+2]]
        i+=2
    print(res)
    t -= 1
