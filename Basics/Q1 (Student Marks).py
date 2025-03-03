marks={
    "Shahid":97,"Kriti":96
}

f=open("students.txt",'w')

for i,j in marks.items():
    f.write(f"{i}:{j}\n")
f.close()

f=open("students.txt",'r')

data=f.read()

print(data)

f.close()
