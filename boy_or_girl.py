name=input()
unique=""
for i in name:
    if i not in unique:
        unique+=i
if len(unique)%2==0:
    print("CHAT WITH HER!")
else:
    print("IGNORE HIM!")
