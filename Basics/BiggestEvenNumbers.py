a=[1,2,3,4,5,6,7,8,9,12,14,17,18,111]

b=[]

for i in a:
    if i%2==0:
        b.append(i)


max=0

for i in b:
    if i>max:
        max=i
    elif len(b)==0:
        print("There are no even numbers in the given list!")
        
print(f"The largest even number given in the list is: {max}")


