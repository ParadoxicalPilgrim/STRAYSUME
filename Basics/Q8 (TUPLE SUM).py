a=[]

n=int(input("How many elements do you want in your tuple?: "))

for i in range(0,n):
    a.append(input(f"Enter element {i+1}: "))

b=tuple(a)

sum=0 

for i in b:
    sum+=int(i)

print(f"Your tuple is: {b} and the sum of the elements in the tuple is: {sum}")


