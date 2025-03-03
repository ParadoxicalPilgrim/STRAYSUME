# STRING ADD

a=str(input("Enter a string: "))
b=str(input("Enter an element you want to search for in the string: "))

hold=''

for i in a:
    if i==b:
        break
    hold+=i

print("The string untill the entered element is: ",hold)

