n=int(input())
totsum=0
for i in range(n):
    p,v,t=map(int,input().split())
    if p==1 and t==1 or p==1 and v==1 or v==1 and t==1:
        totsum+=1
print(totsum)
