s = input()
t = input()
position = 1
for instruction in t:
    if s[position - 1] == instruction:
        position += 1 
print(position)
