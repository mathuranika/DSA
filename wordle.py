t = int(input())

while t > 0:
    S = input()
    T = input()
    M = ""
    for i in range (0,5):
        if S[i] == T[i]:
            M+="G"
        else:
            M+="B"
    print(M)
    t -= 1
