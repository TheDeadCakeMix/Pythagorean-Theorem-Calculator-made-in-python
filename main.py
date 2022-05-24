#Pythagorean Theorem Calculator
#Importing stuff to python go brrrrr
import time
import math
#Taking input from the user
a = input("Pick a value for A: ")
b = input("Pick a value for B: ")
#Changing a and b from strings to ints
a = int(a)
b = int(b)
#calculating a² + b²
c = a ** 2 + b ** 2
#getting the square root of c
c = math.sqrt(c)
#changing c from a int to a string so it can be printed with text
c = str(c)
#print "Calculating" even tho its already done ;)
print("Calculating...")
#wait 1 second
time.sleep(1)
#print C
print("\n C = " + c)