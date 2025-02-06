def age():
    l,b=map(int,input().split())
    year=0
    while l<=b:
        l=3*l
        b=2*b
        year+=1
    print(year)
age()
