import pandas as pd
df = pd.read_csv("data/raw/data.csv")
agg_df = df.groupby("CustomerId").agg({
    "Amount": ["sum", "mean", "count", "std"]
})
agg_df = df.groupby("CustomerId").agg({
    "Amount": ["sum", "mean", "count", "std"]
}).reset_index()

agg_df.columns = [
    "CustomerId",
    "Total_Transaction_Amount",
    "Average_Transaction_Amount",
    "Transaction_Count",
    "Std_Transaction_Amount"
]
df = df.merge(agg_df, on="CustomerId", how="left")
df["TransactionStartTime"] = pd.to_datetime(
    df["TransactionStartTime"]
)

df["transaction_hour"] = df["TransactionStartTime"].dt.hour
df["transaction_day"] = df["TransactionStartTime"].dt.day
df["transaction_month"] = df["TransactionStartTime"].dt.month
df["transaction_year"] = df["TransactionStartTime"].dt.year
from sklearn.impute import SimpleImputer

numeric_imputer = SimpleImputer(strategy="median")
categorical_imputer = SimpleImputer(strategy="most_frequent")
from sklearn.preprocessing import OneHotEncoder
from sklearn.preprocessing import StandardScaler
from sklearn.pipeline import Pipeline
from sklearn.compose import ColumnTransformer
numeric_pipeline = Pipeline([
    ("imputer", SimpleImputer(strategy="median")),
    ("scaler", StandardScaler())
])
categorical_pipeline = Pipeline([
    ("imputer", SimpleImputer(strategy="most_frequent")),
    ("encoder", OneHotEncoder(handle_unknown="ignore"))
])
# Define feature columns

numerical_cols = [
    "Amount",
    "Value",
    "PricingStrategy",
    "transaction_hour",
    "transaction_day",
    "transaction_month",
    "transaction_year",
    "Total_Transaction_Amount",
    "Average_Transaction_Amount",
    "Transaction_Count",
    "Std_Transaction_Amount"
]

categorical_cols = [
    "CurrencyCode",
    "ProviderId",
    "ProductId",
    "ProductCategory",
    "ChannelId"
]
preprocessor = ColumnTransformer([
    ("num", numeric_pipeline, numerical_cols),
    ("cat", categorical_pipeline, categorical_cols)
])
processed_data = preprocessor.fit_transform(df)
from category_encoders.woe import WOEEncoder
snapshot_date = df["TransactionStartTime"].max() + pd.Timedelta(days=1)

rfm = df.groupby("CustomerId").agg({
    "TransactionStartTime":
        lambda x: (snapshot_date - x.max()).days,
    "TransactionId": "count",
    "Amount": "sum"
})

rfm.columns = ["Recency", "Frequency", "Monetary"] 
from sklearn.preprocessing import StandardScaler

scaler = StandardScaler()

rfm_scaled = scaler.fit_transform(rfm)
from sklearn.cluster import KMeans

kmeans = KMeans(
    n_clusters=3,
    random_state=42
)

rfm["Cluster"] = kmeans.fit_predict(rfm_scaled) 
print(
    rfm.groupby("Cluster")[
        ["Recency","Frequency","Monetary"]
    ].mean()
)
HIGH_RISK_CLUSTER = 0

rfm["is_high_risk"] = (
    rfm["Cluster"] == HIGH_RISK_CLUSTER
).astype(int)

print(rfm["is_high_risk"].value_counts())
df = df.merge(
    rfm[["is_high_risk"]],
    left_on="CustomerId",
    right_index=True,
    how="left"
) 
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier
 
from sklearn.model_selection import train_test_split
X = rfm[["Recency", "Frequency", "Monetary"]]

y = rfm["is_high_risk"]

X_train,X_test,y_train,y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)
 