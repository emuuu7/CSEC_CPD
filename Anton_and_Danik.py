def chess():
    no_of_play=int(input())
    anton=0
    danik=0
    results = list(input().upper())
    for i in range(no_of_play):
        if results[i]=="D":
            danik+=1
        elif results[i]=="A":
            anton+=1
        else :
            print("invalid input")
            return
    if anton>danik:
        print("Anton")
    elif anton<danik:
        print("Danik")
    else:
        print("Friendship")
chess()
