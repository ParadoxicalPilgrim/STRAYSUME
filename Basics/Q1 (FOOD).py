fav={}

for i in range(0,4):
    food=input(f"Enter your rank {i+1} favourite food: ")
    fav[i+1]=food

print(f"Your favourite foods ranked: {fav}")
    
yn=input("Do you want to delete any of your favourite foods? (y/n): ")



if yn=="y":
    d=int(input("Enter the rank of the food you want to delete: "))
    for i in fav:
        if i==d:
            del fav[i]
            break

        print(f"Your updated favourite foods ranked: {fav}")

else:
    print(f"Your favourite foods ranked: {fav}")




