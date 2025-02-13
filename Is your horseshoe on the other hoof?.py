c=list(map(int,input().split()))
color=[]
for i in c:
    if i not in color:
        color.append(i)
print(4-len(color))


