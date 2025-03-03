import numpy as np

studs=np.array([('Adsaf',6.0,"1A"),
                ("Fdhas",5.8,"1A"),
                ("Gdgh",5.5,"1C")],
                dtype=[('name',"U10"),('height','f4'),('class','U10')])

sorted_studs=np.sort(studs,order=['class','height'])

print(f"Students: {studs}")
print(f"Sorted students according to given condition: {sorted_studs}")