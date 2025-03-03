import array
from array import *

d = array('i', [1, 2, 3, 4, 5])

print("Array elements:")
for i in d:
    print(i, end=' ')
print()


n = int(input("Select a number from the array: "))
while n not in d:
    print("The number is not in the array. Please try again.")
    n = int(input("Select a number from the array: "))

p= d.index(n)
print(f"The position of {n} in the array is: {p}")
