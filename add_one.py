def solve():
    n_str = input()
    n_list = list(n_str)
    carry = 1
    i = len(n_list) - 1
    while i >= 0 and carry:
        new_digit = int(n_list[i]) + carry
        if new_digit == 10:
            n_list[i] = '0'
            carry = 1
        else:
            n_list[i] = str(new_digit)
            carry = 0
        i -= 1
    if carry:
        n_list.insert(0, '1')
    print("".join(n_list))

t = int(input())
for _ in range(t):
    solve()
