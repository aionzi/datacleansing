import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.preprocessing import StandardScaler

# --- Load Dataset ---

# Read the cleaned dataset from a CSV file
df = pd.read_csv("data-dropna.csv")

# --- Histogram of Sales ---

# Set the size of the plot
plt.figure(figsize=(10, 6))

# Plot a histogram to show the distribution of 'Sales' values
plt.hist(df["Sales"], bins=20, color="skyblue")

# Add a title and axis labels
plt.title("Sales Distribution")
plt.xlabel("Sales Amount")
plt.ylabel("Frequency")

# Display the histogram
plt.show()

print("...")

# --- Scatter Plot: Sales vs Profit ---

# Create a scatter plot to show the relationship between Sales and Profit
# Points are colored by 'Category'
plt.figure(figsize=(10, 6))
sns.scatterplot(x="Sales", y="Profit", hue="Category", data=df)

# Add title and axis labels
plt.title("Sales vs Profit")
plt.xlabel("Sales")
plt.ylabel("Profit")

# Show legend with title
plt.legend(title='Category')

# Display the scatter plot
plt.show()

# --- Box Plot: Sales by Category ---

# Create a box plot to visualize the distribution of Sales within each Category
plt.figure(figsize=(12, 6))
sns.boxplot(x="Category", y="Sales", data=df)

# Add title and axis labels
plt.title("Sales Distribution by Category")
plt.xlabel("Category")
plt.ylabel("Sales")

# Rotate x-axis labels for better readability
plt.xticks(rotation=45)

# Display the box plot
plt.show()

#Bar chart - Total Sales by Discount

plt.figure(figsize=(8, 5))
sales_by_discount = df.groupby("Discount")["Sales"].sum().reset_index()
sns.barplot(x="Discount", y="Sales", hue="Discount", data=sales_by_discount, palette="Blues_d", legend=False)
plt.title("Total Sales by Discount")
plt.xlabel("Discount")
plt.ylabel("Sales")
plt.grid(True)
plt.show()
