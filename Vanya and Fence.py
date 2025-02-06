def fence():
    n , height_of_fence = map(int,input().split())
    x=list(map(int,input().split()))
    min_fence = 0
    for i in range(n):
        if x[i] <= height_of_fence:
            min_fence+=1
        else:
            min_fence+=2
    print(min_fence)
fence()
