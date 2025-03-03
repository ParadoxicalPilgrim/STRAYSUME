s1=set()
s2=set()

n=int(input("Enter the number of elements in the first set: "))

for i in range(n):
    element=input()
    s1.add(element)

m=int(input("Enter the number of elements in the second set: "))
for i in range(m):
    element=input()
    s2.add(element)

union=s1.union(s2)
difference=s1.difference(s2)
inter=s1.intersection(s2)

print(f"\nThe union of the entered sets: {union} ")
print(f"\nThe difference of the entered sets: {difference} ")
print(f"\nThe intersection of the entered sets: {inter} ")
