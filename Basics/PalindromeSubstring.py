s=str(input("Enter a string: "))

p=set()

for i in range(0,len(s)):
    for j in range(1,len(s)+1):
        if s[i:j]==s[i:j][::-1]:
            if (len(s[i:j]))>1:
                p.add(s[i:j])


print(p)


