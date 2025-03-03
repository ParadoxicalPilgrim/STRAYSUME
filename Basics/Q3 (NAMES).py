names=["Shahid Kapoor","Yami Gautam","Kriti Sanon"]
f=open("Name1.txt",'w')
f.write(str(names))
f.close()

f=open("Name1.txt",'r')
data=f.read()
print(data)
f.close()

de=input("Enter the name you want to remove: ").strip()

dataa=[i for i in names if i!=de]

f=open("Name2.txt",'w',newline='')
f.write(str(dataa))
f.close()

f=open("Name2.txt",'r')
dataa=f.read()
print(dataa)
f.close()
