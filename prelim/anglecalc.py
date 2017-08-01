import math

print("Enter the value of the two sides")
a = float(input())
c = float(input())
print("Enter the value of the angle")
ang = float(input())

b = math.sqrt((a**2 + c**2) - 2*a*c*math.cos(ang))

print("The value of the third side is {}".format(b))
