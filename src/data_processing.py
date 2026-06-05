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