n=int(input())
ins=list(map(int, input().split()))
p=0
count=0
for i in range(n):
    if ins[i]<=-1 and p==0:
        count+=1
    elif ins[i]<=-1 and p>=1:
        p-=1
    elif ins[i]>=1:
        p+=ins[i]
print(count)
