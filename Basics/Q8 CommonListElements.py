def commoner(a,b):
    c=[]
    for i in a:
        for j in b:
            if i==j:
                c.append(i)
                
    print("The common elements in the two lists are: ",c)


a=[1,32,3,4,5,56,67,8,9,10]
b=[1,2,3,4,5,6,7,8,9,10]
commoner(a,b)



            
            
        