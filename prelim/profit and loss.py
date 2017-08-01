import math

print("Enter the price of the commodity bought from the store")

x = float(input())

print("Enter the price of the commodity bought from online")

y = float(input())

diff = float(y - x)

if diff > 0:
    print("You got a profit of {}".format(math.fabs(diff)))
else:
    print("You got a loss of {}".format(math.fabs(diff)))
