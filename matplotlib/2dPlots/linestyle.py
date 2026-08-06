import pandas as pd
import matplotlib.pyplot as plt

batsman = pd.read_csv("sharma-kohli.csv")

print(batsman)

# -----------------------------------------------------------
# linestyle = Changes the style of the plotted line
# Common styles:
# "solid"    (Default)
# "dashed"   (--)
# "dotted"   (:)
# "dashdot"  (-.)
# -----------------------------------------------------------

# plt.plot(batsman['index'], batsman['V Kohli'], color="#D9F10F", linestyle="dashed")
# plt.plot(batsman['index'], batsman['RG Sharma'], color="#FC00D6", linestyle="dashed")

# plt.plot(batsman['index'], batsman['V Kohli'], color="#D9F10F", linestyle="dotted")
# plt.plot(batsman['index'], batsman['RG Sharma'], color="#FC00D6", linestyle="dotted")

plt.plot(batsman['index'], batsman['V Kohli'], color="#D9F10F", linestyle="dashdot",linewidth=3)
plt.plot(batsman['index'], batsman['RG Sharma'], color="#FC00D6", linestyle="dashdot",linewidth=2)

# -----------------------------------------------------------
# linewidth = Sets the thickness (width) of the plotted line
# Higher value → Thicker line
# Lower value  → Thinner line
# -----------------------------------------------------------

plt.title("Rohit Sharma vs Virat Kohli")

plt.xlabel("Seasons")
plt.ylabel("Runs Scored")

plt.show()