import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# Generate 50 evenly spaced values from -10 to 10
x = np.linspace(-10, 10, 50)

# Generate Y values with random noise
y = 10 * x + 3 + np.random.randint(0, 300, 50)

print(x)
print(y)

# Create a scatter plot
plt.scatter(x, y)

# -----------------------------------------------------------
# plt.scatter(x, y)
# x = Values for the X-axis
# y = Values for the Y-axis
# -----------------------------------------------------------

# Display the graph
plt.show()