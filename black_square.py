a=list(map(int,input().split()))
st=list(input())
add=0
for i in st:
    add+=a[int(i)-1]
print(add)
