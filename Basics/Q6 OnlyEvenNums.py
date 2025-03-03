a=[]
b=[]

n=int(input("Enter the number of elements in the list: "))

for i in range(n):
    x=int(input("Enter the element: "))
    a.append(x)
    
    
for i in a:
    if i%2==0:
        b.append(i)
        
print("The even numbers in the list are: ",b)