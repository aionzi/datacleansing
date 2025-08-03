import pandas as pd

# Load the dataset from a CSV file
df = pd.read_csv("messy_dataset.csv")

# --- Handling Missing Values ---

# Fill missing 'Name' values with the most frequent value (mode)
a = df["Name"].mode()
a = df.fillna({"Name": a}, inplace=True)

# Fill missing 'Age' values with the median
b = df["Age"].median()
b = df.fillna({"Age": b}, inplace=True)

# Fill missing 'Sales' values with the mean
c = df["Sales"].mean()
c = df.fillna({"Sales": c}, inplace=True)

# Fill missing 'Profit' values with the mean
d = df["Profit"].mean()
d = df.fillna({"Profit": d}, inplace=True)

# Fill missing 'Date' values with the most frequent value (mode)
e = df["Date"].mode()
e = df.fillna({"Date": e}, inplace=True)

# Fill missing 'Category' values with the most frequent value (mode)
f = df["Category"].mode()
f = df.fillna({"Category": f}, inplace=True)

# Fill missing 'Discount' values with the most frequent value (mode)
g = df["Discount"].mode()
g = df.fillna({"Discount": g}, inplace=True)


# Print a boolean Series indicating duplicate rows
print(df.duplicated())

# Remove duplicate rows from the DataFrame
df.drop_duplicates(inplace=True)

# --- Data Type Conversion ---

# Convert 'Date' column to datetime format, coercing errors to NaT
df["Date"] = pd.to_datetime(df["Date"], errors='coerce')

# Display the cleaned DataFrame
print(df)

# Save the cleaned DataFrame to a new CSV file
df.to_csv('data-dropna.csv', index=False)

# --- Outlier Detection and Removal (using IQR method) ---

# Calculate the first (Q1) and third (Q3) quartiles for 'Sales'
Q1 = df["Sales"].quantile(0.25)
Q3 = df["Sales"].quantile(0.75)

# Compute the Interquartile Range (IQR)
IQR = Q3 - Q1

# Filter out rows where 'Sales' values are outside 1.5*IQR from Q1 and Q3
df = df[~((df["Sales"] < (Q1 - 1.5 * IQR)) | (df["Sales"] > (Q3 + 1.5 * IQR)))]
