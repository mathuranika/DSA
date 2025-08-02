t = int(input())

while t > 0:
    n = int(input())
    s = input()
    server = "A"
    a_pts = 0
    b_pts = 0
    for i in s:
        if i == server:
            if i == "A":
                a_pts += 1
            else:
                b_pts += 1
        else:
            if server == "A":
                server = "B"
            else:
                server = "A"
    print(a_pts, b_pts)
    t -= 1
