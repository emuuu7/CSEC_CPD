k,r=map(int,input().split())
count=1
price=k
while price%10!=r and price%10!=0:
    count+=1
    price=count*k
print(count)
