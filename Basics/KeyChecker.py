d = {2: 56, 1: 2, 3: 323}

search=int(input("Enter a key to search for in the dictionary: "))

count=0

for i in d:
    if i==search:
        print("Key found!")
        count+=1
        break
        

if count==0:
    print("Key not found!")
    
    