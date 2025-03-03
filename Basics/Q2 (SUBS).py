n=int(input("How many subjects do you have?"))
l=[]

for i in range(0,n):
    sub=input(f"Enter the name of subject {i+1}: ")
    l.append(sub)

print(f"Your subjects are: {l}")

yn=input("Do you hate any of your subjects? (y/n): ")

if yn=='y':
    name=input("Enter the name of the subject: ")
    for i in l:
        if i==name:
            l.remove(i)
    print(f"Your subjects after removing the subject you hate is: {l}")
else:
    print(f"Here are your subjects again: {l}")


