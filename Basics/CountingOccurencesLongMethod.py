list= [1,2,3,4,5,5,6,7,8,8,9,9,9,9,9,9,1,2,3,4,5,6,6,6]

count=0

for i in range(len(list)):
    if list[i]==8:
        count+=1

print(count)

