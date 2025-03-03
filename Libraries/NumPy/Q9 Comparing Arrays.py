import numpy as np

arr1=np.array([1,2,3,4,5])
arr2=np.array([1,2,4,7,8])

great=np.greater(arr1,arr2)
equal=np.equal(arr1,arr2)
lesser=np.less(arr1,arr2)

print(f"The values equal in the array:{equal}, greater in array 1 than array 2:{great}, smaller in array 1 than array 2:{lesser}")
