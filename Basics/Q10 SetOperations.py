def set_operations(s1,s2):
    a=set()
    b=set()
    c=set()
    
    for i in range(s1):
        x=int(input("Enter the element: "))
        a.add(x)
        
    print("Enter the elements of the second set: ")
        
    for i in range(s2):
        x=int(input("Enter the element: "))
        b.add(x)
        
    c=a.intersection(b)
    
    print("The common elements in the two sets are: ",c)
    print("The union of the two sets is: ",a.union(b))
    print("The difference between the two sets is: ",a.difference(b))
    
    
    
s1=int(input("Enter the number of elements in the first set: "))
s2=int(input("Enter the number of elements in the second set: "))
set_operations(s1,s2)