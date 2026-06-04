import pandas as pd

df = pd.read_csv("data/raw/08_investor_transactions.csv")

# date format
df["transaction_date"] = pd.to_datetime(
    df["transaction_date"]
)

# standardize transaction types
df["transaction_type"] = (
    df["transaction_type"]
    .str.strip()
    .str.upper()
)

# amount > 0
df = df[df["amount_inr"] > 0]

# valid kyc values
valid_kyc = ["Verified", "Pending"]

invalid = df[
    ~df["kyc_status"].isin(valid_kyc)
]

print("Invalid KYC Records:")
print(len(invalid))
print("KYC Values:")
print(df["kyc_status"].value_counts())

# remove duplicates
df = df.drop_duplicates()

df.to_csv(
    "data/processed/08_investor_transactions_clean.csv",
    index=False
)

print("Saved:", df.shape)