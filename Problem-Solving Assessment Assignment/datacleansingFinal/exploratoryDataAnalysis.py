import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.preprocessing import StandardScaler

# --- Load Dataset ---

# Read the cleaned dataset from a CSV file
df = pd.read_csv("data-dropna.csv")

# Display the first 5 rows of the dataset
print(df.head(5))
print("...")

# --- Descriptive Statistics ---

# Generate summary statistics for numerical columns
summary_statistics = df.describe()
print(summary_statistics)
print("...")

# --- Correlation Analysis ---

# Compute the correlation matrix from the summary statistics
correlation_matrix = df.corr(numeric_only=True)
print(correlation_matrix)
print("...")


# --- Pivot Table: Sales by Category and Discount ---

# Create a pivot table showing total sales by Category and Discount levels
sales_pivot = df.pivot_table(
    values="Sales",         # The value to aggregate
    index="Category",       # Rows: product categories
    columns="Discount",     # Columns: discount levels
    aggfunc="sum"           # Aggregation function: sum of sales
)

# Display the pivot table
print(sales_pivot)

# --- Visualization: Correlation Heatmap ---

# Set the size of the plot
plt.figure(figsize=(8, 6))

# Create a heatmap of the correlation matrix with annotations and color gradient for extra user readability. 
sns.heatmap(correlation_matrix, annot=True, cmap='YlGnBu', fmt=".2f", linewidths=0.5)

# Set the title of the heatmap
plt.title("Correlation Matrix Heatmap")

# Display the plot
plt.show()

print("...")


