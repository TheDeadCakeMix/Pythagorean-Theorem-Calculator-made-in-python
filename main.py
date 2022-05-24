import time
import math
a = input("Pick a value for A: ")
b = input("Pick a value for B: ")
a = int(a)
b = int(b)
c = a ** 2 + b ** 2
c = math.sqrt(c)
c = str(c)
print("Calculating...")
time.sleep(1)
print("\n C = " + c)