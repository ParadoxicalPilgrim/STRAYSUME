import array as a

numbers=a.array('i',[11,13,18,9,10])

search=int(input("Enter the number you want the position of: "))

for i in range(len(numbers)):
    if numbers[i]==search:
        print(f"Index {i} ")
        
