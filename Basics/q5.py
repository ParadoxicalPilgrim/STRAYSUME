# NOTES QUESTION

notes=[100,50,10,5,2,1]

change=int(input("Enter the amount of change: "))

count=0


for i in notes:
    if change>=i:
        countt=change//i
        count+=countt
        change-=countt*i



print(f"The total amount of notes will be: {count}")


