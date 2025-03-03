import csv

file = open('Books.csv', 'r')
reader = csv.reader(file)
data = list(reader)
file.close()

print("Current data:")
for index, row in enumerate(data):
    print(f"{index}: {row}")

row_to_delete = int(input("Enter the row number to delete: "))
while row_to_delete <= 0 or row_to_delete >= len(data):
    print("Invalid row number. Please try again.")
    row_to_delete = int(input("Enter the row number to delete: "))

data.pop(row_to_delete)


print("\nUpdated data:")
for index, row in enumerate(data):
    print(f"{index}: {row}")

row_to_change = int(input("\nEnter the row number to change: "))
while row_to_change <= 0 or row_to_change >= len(data):
    print("Invalid row number. Please try again.")
    row_to_change = int(input("Enter the row number to change: "))

column_to_change = int(input("Enter the column number to change (0=Title, 1=Author, 2=Year): "))
while column_to_change < 0 or column_to_change > 2:
    print("Invalid column number. Please try again.")
    column_to_change = int(input("Enter the column number to change (0=Title, 1=Author, 2=Year): "))

new_value = input("Enter the new value: ")
data[row_to_change][column_to_change] = new_value

file = open('Books.csv', 'w', newline='')
writer = csv.writer(file)
writer.writerows(data)
file.close()

print("\nData has been updated and written back to Books.csv.")
