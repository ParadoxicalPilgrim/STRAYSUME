import array
from array import *

numbers = array('i', [])

while len(numbers) < 5:
    n = int(input("Enter a number between 10 and 20: "))
    
    if 10 <= n <= 20:
        numbers.append(n)
    else:
        print("Outside the range")


for number in numbers:
    print(number,end=' ')
