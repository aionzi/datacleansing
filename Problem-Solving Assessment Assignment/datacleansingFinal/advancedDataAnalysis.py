import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error


df = pd.read_csv("data-dropna.csv")


def perform_kmeans_clustering(df, n_clusters=3):
    print("\n--- Performing KMeans Clustering ---")
    
    # Select features for clustering
    features = ["Age", "Sales", "Profit", "Discount"]
    clustering_data = df[features].dropna()

    # Standardise the features for fair comparison
    scaler = StandardScaler()
    scaled_features = scaler.fit_transform(clustering_data)

    # Apply KMeans
    kmeans = KMeans(n_clusters=n_clusters, random_state=42, n_init=10)
    cluster_labels = kmeans.fit_predict(scaled_features)

    # Add cluster labels to the dataframe
    df.loc[clustering_data.index, "Cluster"] = cluster_labels

    print("KMeans clustering completed. Added 'Cluster' column.")
    return df


def predict_missing_sales(df):
    print("\n--- Predicting Missing Sales with Linear Regression ---")
    
    # Identify rows with missing Sales
    missing_sales = df[df["Sales"].isna()]
    not_missing_sales = df[df["Sales"].notna()]

    if missing_sales.empty:
        print("No missing Sales values to predict.")
        return df

    # Features and target
    features = ["Profit", "Discount", "Age"]
    X_train = not_missing_sales[features]
    y_train = not_missing_sales["Sales"]
    X_pred = missing_sales[features]

    # Train Linear Regression model
    model = LinearRegression()
    model.fit(X_train, y_train)

    # Predict and fill missing sales
    predicted_sales = model.predict(X_pred)
    df.loc[missing_sales.index, "Sales"] = predicted_sales

    print(f"Predicted and filled {len(missing_sales)} missing Sales values.")
    return df

def generate_advanced_correlation_heatmap(df):
    print("\n--- Generating Advanced Feature Correlation Heatmap ---")

    numeric_df = df.select_dtypes(include=[float, int])
    correlation_matrix = numeric_df.corr()

    plt.figure(figsize=(10, 8))
    sns.heatmap(correlation_matrix, annot=True, cmap='YlGnBu', fmt=".2f", linewidths=0.5)
    plt.title("Advanced Feature Correlation Heatmap")
    plt.tight_layout()
    plt.show()

    print("Displayed advanced heatmap of feature correlations.")


print("\n--- Advanced Data Analysis ---")
df = perform_kmeans_clustering(df)
generate_advanced_correlation_heatmap(df)



