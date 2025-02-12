n=int(input())
count=0
k=input()
for i in range(n-1):
    j=input()
    if j==k:
        continue
    else:
        count+=1
        k=j
print(count+1)
