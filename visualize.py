import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load data
data = pd.read_csv("sample_data.csv")

# Plot
sns.barplot(x="Category", y="Value", data=data)
plt.title("Sample Data Visualization")
plt.savefig("plot.png")  # Save the plot
plt.show()