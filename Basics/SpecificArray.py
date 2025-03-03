import array as a

numbers=a.array('i')

while len(numbers)<5:
    num=int(input("Enter the number to add into the array:"))

    if 10<=num<=20:
        numbers.append(num)
    
    else:
        print("Entered number out of range.")
    
for i in numbers:
    print(i)
    