# Import the Pandas library for data handling
import pandas as pd

# Import the Matplotlib pyplot module for creating graphs
import matplotlib.pyplot as plt

# Apply the 'classic' plotting style
# By default, Matplotlib uses the 'default' style
# plt.style.use('classic')

# Read the CSV file into a Pandas DataFrame
batsman = pd.read_csv("sharma-kohli.csv")

# Display the dataset
print(batsman)

# -----------------------------------------------------------
# Plot a single numerical variable (Virat Kohli's runs)
# X-axis : Match Index (Season)
# Y-axis : Virat Kohli's Runs
# -----------------------------------------------------------
# plt.plot(batsman['index'], batsman['V Kohli'])

# -----------------------------------------------------------
# Plot multiple numerical variables on the same graph
# X-axis : Match Index (Season)
# Y-axis : Runs scored by both batsmen
# -----------------------------------------------------------
plt.plot(batsman['index'], batsman['V Kohli'])
plt.plot(batsman['index'], batsman['RG Sharma'])

# Add a title to the graph
plt.title("Rohit Sharma vs Virat Kohli")

# Label the X-axis
plt.xlabel("Seasons")

# Label the Y-axis
plt.ylabel("Runs Scored")

# Display the line graph
plt.show()