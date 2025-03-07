import matplotlib.pyplot as plt

x_values = list(range(1, 5000))
y_values = [x**3 for x in x_values]

plt.scatter(x_values, y_values, edgecolor='none', s=40)

plt.title("Cubes", fontsize=24)
plt.xlabel("Values", fontsize=14)
plt.ylabel("Cubic Value", fontsize=14)

plt.tick_params(axis='both', which='major', labelsize=14)

plt.show()
