# Mutual Fund Analytics Data Dictionary

## 01_fund_master.csv

| Column        | Data Type | Description                    |
| ------------- | --------- | ------------------------------ |
| amfi_code     | Integer   | Unique AMFI scheme identifier  |
| fund_house    | Text      | Mutual fund company name       |
| scheme_name   | Text      | Name of the mutual fund scheme |
| category      | Text      | Equity or Debt                 |
| sub_category  | Text      | Scheme category                |
| risk_category | Text      | Risk classification            |

## 02_nav_history.csv

| Column    | Data Type | Description          |
| --------- | --------- | -------------------- |
| amfi_code | Integer   | Scheme identifier    |
| date      | Date      | NAV observation date |
| nav       | Decimal   | Net Asset Value      |

## 07_scheme_performance.csv

| Column            | Data Type | Description              |
| ----------------- | --------- | ------------------------ |
| return_1yr_pct    | Decimal   | 1-year return percentage |
| return_3yr_pct    | Decimal   | 3-year return percentage |
| return_5yr_pct    | Decimal   | 5-year return percentage |
| expense_ratio_pct | Decimal   | Fund expense ratio       |
| aum_crore         | Integer   | Assets under management  |

## 08_investor_transactions.csv

| Column           | Data Type | Description                |
| ---------------- | --------- | -------------------------- |
| investor_id      | Text      | Unique investor identifier |
| transaction_date | Date      | Date of transaction        |
| transaction_type | Text      | SIP, Lumpsum or Redemption |
| amount_inr       | Decimal   | Transaction amount         |
| state            | Text      | Investor state             |
| city             | Text      | Investor city              |
| kyc_status       | Text      | Verified or Pending        |
