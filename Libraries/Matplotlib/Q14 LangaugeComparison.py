import matplotlib.pyplot as plt
import numpy as np

lang=np.array(["JavaScript","Python","PHP","Java","C#","C++"])
pops=np.array([22.2, 17.6, 8.8, 8, 7.7, 6.7])

plt.barh(lang,pops,color='black',height=0.5)
plt.title("Most popular programming languages")
plt.xlabel("Programming Languages")
plt.ylabel("Popularity")
plt.show()