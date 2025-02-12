current = ord('a')
rot = 0
word = input()
for char in word:
    target = ord(char)
    clockwise = abs(target - current)
    counterclockwise = 26 - clockwise
    rot+= min(clockwise, counterclockwise)
    current = target
print(rot)
