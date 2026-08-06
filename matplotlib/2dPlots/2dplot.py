# Store car prices (Y-axis values)
price = [48000, 54000, 57000, 49000, 47000, 45000]

# Store corresponding years (X-axis values)
year = [2015, 2016, 2017, 2018, 2019, 2020]

# Import the Matplotlib pyplot module
import matplotlib.pyplot as plt

# Create a 2D line plot of Price against Year
plt.plot(year, price)

# Display the graph
plt.show()