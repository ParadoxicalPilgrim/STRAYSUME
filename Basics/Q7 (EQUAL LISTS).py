n=int(input("How many elements do you want in your first list?: "))
m=int(input("How many elements do you want in your second list?: "))

l1=[]
l2=[]

for i in range(0,n):
    l1.append(input(f"Enter element {i+1}: "))

for i in range(0,m):
    l2.append(input(f"Enter element {i+1}: "))

if len(l1)!=len(l2):
    print("The lists are not equal!")

if l1==l2:
    print("The lists are equal!")

else:
    print("The lists are not equal!")