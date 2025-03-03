import csv

sales_info = {}

initial_data = [
    ["A", 10, 100],
    ["B", 5, 50],
    ["C", 8, 80]
]

file = open('sales_data.csv', mode='w', newline='')
csv_writer = csv.writer(file)

for i in initial_data:
    csv_writer.writerow(i)
file.close()

file = open('sales_data.csv', mode='r')
csv_reader = csv.reader(file)

for i in csv_reader:
    product_name = i[0]
    quantity_sold = int(i[1])
    total_sales = float(i[2])

    sales_info[product_name] = [quantity_sold, total_sales]

file.close()

print(sales_info)
