set1 = set()
set2 = set()

n = int(input("Enter the number of elements in the first set: "))
print("Enter the elements of the first set:")
for i in range(n):
    element = input()
    set1.add(element)


m=int(input("Enter the number of elements in the second set: "))
print("Enter the elements of the second set:")
for i in range(m):
    element = input()
    set2.add(element)

intersection = set1.intersection(set2)


print("\nThe intersection of the entered sets: ")
print(intersection)
