import csv

sales_info={}

f=open("products.txt",'r')
csv_reader=csv.reader(f)

next(csv_reader)

for i in csv_reader:
    product=i[0]
    qty_sold=int(i[1])
    total=float(i[2])
    
    
sales_info[product]=[qty_sold,total]

f.close()

print(sales_info)