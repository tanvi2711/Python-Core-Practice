import pandas as pd

import matplotlib.pyplot as plt

batsman = pd.read_csv("sharma-kohli.csv")

print(batsman)

plt.plot(batsman['index'], batsman['V Kohli'],
         color="#D9F10F", linestyle="dashdot", linewidth=3,
         marker='.', markersize=10,
         label="Virat")  # label = Assigns a name to this line for the legend

plt.plot(batsman['index'], batsman['RG Sharma'],
         color="#FC00D6", linestyle="dashdot", linewidth=2,
         marker='.',
         label="Rohit")  # label = Assigns a name to this line for the legend

# -----------------------------------------------------------
# loc = Sets the position of the legend on the graph
# Common positions:
# 'best'         (Default)
# 'upper right'
# 'upper left'
# 'lower right'
# 'lower left'
# 'right'
# 'center left'
# 'center right'
# 'lower center'
# 'upper center'
# 'center'
# -----------------------------------------------------------

plt.legend(loc='upper right')  # Display the legend on the right side of the graph


plt.title("Rohit Sharma vs Virat Kohli")

plt.xlabel("Seasons")

plt.ylabel("Runs Scored")

plt.show()