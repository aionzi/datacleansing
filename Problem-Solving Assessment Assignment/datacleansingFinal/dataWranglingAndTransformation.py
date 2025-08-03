import pandas as pd

# --- Load and Prepare Dataset ---

# Read the cleaned dataset from a CSV file
df = pd.read_csv("data-dropna.csv")

# Drop unnecessary columns to simplify the dataset
# Columns removed: 'Name', 'Age', 'Gender', 'Date', and 'Discount'
df.drop(columns=['Name','Age', 'Gender', 'Date', 'Discount'], inplace=True)

# --- Grouping and Aggregation ---

# Group data by 'Category' and calculate the total sales for each category
# The result is stored in a new DataFrame 'sales_summary'
sales_summary = df.groupby("Category")["Sales"].sum().reset_index()

# Display the first 10 rows of the DataFrame to inspect
print("\n <---------- DataFrame Summary with Relevant Columns ---------->")
print(df.head(10))

# Display the aggregated sales summary by category
print("\n <---------- Sales Summary ---------->")
print(sales_summary)

# --- Feature Engineering ---

# Create a new column 'Profit Margin' by dividing Profit by Sales
# This calculation avoids division by zero by returning 0 when Sales is 0
df["Profit Margin"] = df.apply(lambda x: x["Profit"] / x["Sales"] if x["Sales"] != 0 else 0, axis=1)


# Display the updated DataFrame with the new 'Profit Margin' column
print("\n <---------- Profit Margin Summary ---------->")
print(df.head(10))
