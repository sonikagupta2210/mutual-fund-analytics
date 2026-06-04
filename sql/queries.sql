-- 1. Top 5 funds by AUM
SELECT scheme_name, aum_crore
FROM fact_performance
ORDER BY aum_crore DESC
LIMIT 5;

-- 2. Average NAV per fund
SELECT amfi_code, AVG(nav) AS avg_nav
FROM fact_nav
GROUP BY amfi_code;

-- 3. Monthly average NAV
SELECT substr(date,1,7) AS month,
AVG(nav) AS avg_nav
FROM fact_nav
GROUP BY month;

-- 4. Total transaction amount by type
SELECT transaction_type,
SUM(amount_inr) AS total_amount
FROM fact_transactions
GROUP BY transaction_type;

-- 5. Transactions by state
SELECT state,
COUNT(*) AS total_transactions
FROM fact_transactions
GROUP BY state
ORDER BY total_transactions DESC;

-- 6. Funds with expense ratio below 1%
SELECT scheme_name, expense_ratio_pct
FROM fact_performance
WHERE expense_ratio_pct < 1;

-- 7. Average return by category
SELECT category,
AVG(return_3yr_pct) AS avg_return
FROM fact_performance
GROUP BY category;

-- 8. Top 5 funds by 5-year return
SELECT scheme_name, return_5yr_pct
FROM fact_performance
ORDER BY return_5yr_pct DESC
LIMIT 5;

-- 9. Total investment amount by KYC status
SELECT kyc_status,
SUM(amount_inr) AS total_amount
FROM fact_transactions
GROUP BY kyc_status;

-- 10. Count of funds by risk grade
SELECT risk_grade,
COUNT(*) AS total_funds
FROM fact_performance
GROUP BY risk_grade;
