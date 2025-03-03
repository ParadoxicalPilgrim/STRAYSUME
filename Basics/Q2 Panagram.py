letters=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
x=input("Enter a string: ")
y=x.lower()

for i in y:
    if i in letters:
        letters.remove(i)
        
if len(letters)==0:
    print("The given string is a panagram!")
    
else:
    print("The given string is not a panagram!")


    

    
    