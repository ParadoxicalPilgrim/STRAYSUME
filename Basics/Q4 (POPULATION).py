countries={"China":143, "India":136, "USA":32, "Pakistan":21}

print("ENTER YOUR CHOICE: \n")

print("1. Display the population of all countries")
print("2. Add a country")
print("3. Remove a country")
print("4. Query a country")

choice = int(input())

if choice == 1:
    for i,j in countries.items():
        print(i,"==>",j)

elif choice == 2:
    country = input("Enter the name of the country: ")
    population = int(input("Enter the population of the country: "))
    countries[country]=population

elif choice == 3:
    country = input("Enter the name of the country you want to remove: ")
    countries.pop(country)

elif choice==4:
    country=input("Enter the name of the country you want to query: ")
    print(countries[country])