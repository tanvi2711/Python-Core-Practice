import pandas as pd

import matplotlib.pyplot as plt

batsman = pd.read_csv("sharma-kohli.csv")

print(batsman)

# -----------------------------------------------------------
# marker = Adds symbols at each data point on the plotted line
# Here we demonstrate different marker styles:
# 'D' = Diamond
# '+' = Plus
# '.' = Point
# -----------------------------------------------------------

# Plot using Diamond (D) markers
# plt.plot(batsman['index'], batsman['V Kohli'],
#          color="#D9F10F", linestyle="dashdot", linewidth=3, marker='D')
# plt.plot(batsman['index'], batsman['RG Sharma'],
#          color="#FC00D6", linestyle="dashdot", linewidth=2, marker='D')

# # Plot using Plus (+) markers
# plt.plot(batsman['index'], batsman['V Kohli'],
#          color="#D9F10F", linestyle="dashdot", linewidth=3, marker='+')
# plt.plot(batsman['index'], batsman['RG Sharma'],
#          color="#FC00D6", linestyle="dashdot", linewidth=2, marker='+')

# Plot using Point (.) markers
plt.plot(batsman['index'], batsman['V Kohli'],
         color="#D9F10F", linestyle="dashdot", linewidth=3, marker='.',markersize=10)
plt.plot(batsman['index'], batsman['RG Sharma'],
         color="#FC00D6", linestyle="dashdot", linewidth=2, marker='.')

# -----------------------------------------------------------
# markersize = Sets the size of the marker
# Higher value → Larger marker
# Lower value  → Smaller marker
# Default value = 6
# -----------------------------------------------------------


plt.title("Rohit Sharma vs Virat Kohli")

plt.xlabel("Seasons")

plt.ylabel("Runs Scored")

plt.show()

# -----------------------------------------------------------
# marker = Adds symbols at each data point on the line
#
# Common marker styles:
# '.'  = Point
# ','  = Pixel
# 'o'  = Circle
# 'v'  = Triangle Down
# '^'  = Triangle Up
# '<'  = Triangle Left
# '>'  = Triangle Right
# '1'  = Tri Down
# '2'  = Tri Up
# '3'  = Tri Left
# '4'  = Tri Right
# 's'  = Square
# 'p'  = Pentagon
# '*'  = Star
# 'h'  = Hexagon 1
# 'H'  = Hexagon 2
# '+'  = Plus
# 'x'  = X
# 'X'  = Filled X
# 'D'  = Diamond
# 'd'  = Thin Diamond
# '|'  = Vertical Line
# '_'  = Horizontal Line
#
# Default : No marker
# -----------------------------------------------------------