n = int(input().strip())
teams = [tuple(map(int, input().split())) for _ in range(n)]
count = 0
for i in range(n):
    host= teams[i][0]
 
    for j in range(n):
        if i != j:
            guest = teams[j][1]
            if host == guest:
                count += 1 
print(count)
