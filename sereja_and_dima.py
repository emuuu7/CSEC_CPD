n = int(input())
no = list(map(int, input().split()))
s = 0
d = 0
turn = 0
while no:
    if no[0] >= no[-1]:
        chosen = no.pop(0)
    else:
        chosen = no.pop()
    if turn % 2 == 0:
        s += chosen
    else:
        d += chosen
    turn += 1
print(f"{s} {d}")
