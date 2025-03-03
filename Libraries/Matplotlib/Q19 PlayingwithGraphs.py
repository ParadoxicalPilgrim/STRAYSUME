import matplotlib.pyplot as plt

x = [1, 2, 3, 4, 5]
y = [2, 3, 5, 7, 11]
z = [1, 4, 6, 8, 10]
a = [3, 5, 9, 11, 14]

plt.plot(x, y, label='Line 1', color='pink', linewidth=2)
plt.plot(x, z, label='Line 2', color='black', linewidth=3)
plt.plot(x, a, label='Line 3', color='red', linewidth=1)

plt.title('Multiple Lines with Legends, Different Widths, and Colors')
plt.xlabel('X-axis')
plt.ylabel('Y-axis')

plt.legend()
plt.show()
