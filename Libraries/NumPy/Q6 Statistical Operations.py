import numpy as np

arr=np.array([[1,2,3],
              [4,5,6],
              [7,8,9]])

mean=np.mean(arr,axis=1)
std_devn=np.std(arr,axis=1)
vrnce=np.var(arr,axis=1)

print(f"The mean is: {mean}")
print(f"The standard deviation is: {std_devn}")
print(f"The variance is: {vrnce}")
