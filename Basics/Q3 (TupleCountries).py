countries=('nz','ind','sa','arg','ger')
print(countries)

name=input("Enter any of the countries displayed above: ")
count=0

for i in countries:
    if i!=name:
        count+=1
    if i==name:
        print(f"The index of the country is: {count}")

        






