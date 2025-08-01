t = int(input())
def isHappy(s):
    vowels = ['a','e','i','o','u']
    for i in range(len(s)-2):
        if s[i] in vowels:
            if s[i+1] in vowels and s[i+2] in vowels:
                return "HAPPY"
    return "SAD"
    
while t > 0:
    s = input()
    print(isHappy(s))
    t -= 1
