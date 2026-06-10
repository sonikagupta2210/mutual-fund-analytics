import pandas as pd
import sqlite3

# Database connection
conn = sqlite3.connect("../bluestock_mf.db")

# Load performance data
performance_df = pd.read_sql(
    "SELECT * FROM fact_performance",
    conn
)

# User input
risk = input(
    "Enter Risk Appetite (Low/Moderate/High): "
)

# Recommendations
recommendations = (
    performance_df[
        performance_df["risk_grade"].str.lower()
        ==
        risk.lower()
    ]
    .sort_values(
        "sharpe_ratio",
        ascending=False
    )
    .head(3)
)

print("\nTop 3 Recommended Funds:\n")

print(
    recommendations[
        [
            "scheme_name",
            "fund_house",
            "risk_grade",
            "sharpe_ratio"
        ]
    ]
)