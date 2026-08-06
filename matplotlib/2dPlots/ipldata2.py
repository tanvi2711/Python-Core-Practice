import pandas as pd
import matplotlib.pyplot as plt

batsman = pd.read_csv("sharma-kohli.csv")

print(batsman)

# Plot Virat Kohli's runs with a custom HEX color
plt.plot(batsman['index'], batsman['V Kohli'], color="#D9F10F")

# Plot Rohit Sharma's runs with a custom HEX color
plt.plot(batsman['index'], batsman['RG Sharma'], color="#FC00D6")

plt.title("Rohit Sharma vs Virat Kohli")

plt.xlabel("Seasons")
plt.ylabel("Runs Scored")

plt.show()