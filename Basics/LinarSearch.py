x=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]

target=int(input("Enter the target element: "))

for i in range(0,len(x)):
    if target==x[i]:
        print(f"Element found at index: {i}")


