import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


# --- Load Dataset ---
df = pd.read_csv("data-dropna.csv")


# Interactive Filtering
category = input("Enter a category to filter (Electronics, Clothing, etc.): ")
filtered_df = df[df["Category"] == category]

# Generate dynamic Visualisation
plt.figure(figsize=(10, 6))
sns.barplot(x="Discount", y="Sales", data=filtered_df, ci=None)
plt.title(f"Sales Distribution for {category}")
plt.xlabel("Discount Level")
plt.ylabel("Sales")
plt.show()


