a=set()
b=set()
c=set()

n=int(input("Enter the number of elements in the first set: "))
m=int(input("Enter the number of elements in the second set: "))

for i in range(n):
    x=int(input("Enter the element: "))
    a.add(x)
    
print("Enter the elements of the second set: ")
    
for i in range(m):
    x=int(input("Enter the element: "))
    b.add(x)
    
c=a.intersection(b)

print("The common elements in the two sets are: ",c)
    