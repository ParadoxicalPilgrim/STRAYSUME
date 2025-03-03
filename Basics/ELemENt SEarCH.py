mylist=[1,2,3,4,5,6,7,8,9]

target=int(input("Enter a number to search for its existence: "))

count=0

for i in range(len(mylist)):
    if target==mylist[i]:
        count+=1
        print(f"Element found at index: {i}")


if (count==0):
    print("Element not found!")

    