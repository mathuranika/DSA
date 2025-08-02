def solve():
    n = int(input())
    doll_counts = {}
    for _ in range(n):
        doll_type = int(input())
        if doll_type in doll_counts:
            doll_counts[doll_type] += 1
        else:
            doll_counts[doll_type] = 1
    
    for doll_type, count in doll_counts.items():
        if count % 2 != 0:
            print(doll_type)
            return

t = int(input())
for _ in range(t):
    solve()
