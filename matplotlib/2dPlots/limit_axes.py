price = [48000, 54000, 57000, 49000, 47000, 45000,4500000]

year = [2015, 2016, 2017, 2018, 2019, 2020,2021]

import matplotlib.pyplot as plt

plt.plot(year, price)

# ylim() = Sets the minimum and maximum limits of the Y-axis
plt.ylim(0, 75000)

# xlim() = Sets the minimum and maximum limits of the X-axis
plt.xlim(2017, 2020)

# -----------------------------------------------------------
# grid() = Displays grid lines on the graph
# Helps in reading and comparing data values
# -----------------------------------------------------------
plt.grid()

plt.show()

