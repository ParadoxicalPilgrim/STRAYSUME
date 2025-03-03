import numpy as np
import matplotlib.pyplot as plt

x=np.random.rand(10)
y=np.random.rand(10)

plt.scatter(x,y,color="pink")

plt.title("Scatter Plot of Random Values")
plt.xlabel("X-axis")
plt.ylabel("Y-axis")

plt.show()
