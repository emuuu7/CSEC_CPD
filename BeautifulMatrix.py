mat = []
for i in range(5):
    row = list(map(int, input().split()))
    mat.append(row)
for i in range(5):
    for j in range(5):
        if mat[i][j] == 1:
            x, y = i, j
            
moves = abs(x - 2) + abs(y - 2)
print(moves)
