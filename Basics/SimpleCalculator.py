a=float(input("Enter a number: "))
b=float(input("Enter another number: "))

print("Select an option from below: ")

print("1.Add")
print("2.Subtract")
print("3.Mulitply")
print("4.Divide")

ch=int(input("Enter your choice: "))
if ch==1:
    print(a+b)
elif ch==2:
    print(a-b)
elif ch==3:
    print(a*b)
elif ch==4:
    print(a/b)
else:
    print("Invalid choice!")


    