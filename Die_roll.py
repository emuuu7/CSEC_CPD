import math
y,w=map(int,input().split())
s=max(y,w)
p=7-s
gcd_value = math.gcd(p, 6)  # Find the greatest common divisor
# Print the fraction in reduced form
print(f"{p // gcd_value}/{6 // gcd_value}")
