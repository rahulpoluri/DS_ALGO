-- SQL practice on bank_seed.sql (open-banking style schema)
-- Run order reminder: FROM -> WHERE -> GROUP BY -> HAVING -> SELECT -> ORDER BY
--   WHERE filters rows, HAVING filters groups; aliases usable in ORDER BY, NOT in HAVING (Postgres).

-- Q1. Total spent (outgoing only) per category, highest first; NULL category -> 'uncategorised'
SELECT COALESCE(category, 'uncategorised') AS category,
       ABS(SUM(amount)) AS total_spent
FROM transactions
WHERE amount < 0
GROUP BY category
ORDER BY total_spent DESC;

-- Q2. Duplicate bank transactions (same account + bank_tx_id)
SELECT account_id, bank_tx_id, COUNT(*) AS times
FROM transactions
GROUP BY account_id, bank_tx_id
HAVING COUNT(*) > 1;
-- Prevent at write time: UNIQUE (account_id, bank_tx_id) + INSERT ... ON CONFLICT DO NOTHING (idempotent sync)

-- Q3. Every account with owner, bank and transaction count (0 for accounts with none)
SELECT eu.name, a.bank_name, COUNT(t.id) AS tx_count
FROM accounts a
JOIN end_users eu        ON a.end_user_id = eu.id
LEFT JOIN transactions t ON t.account_id = a.id
GROUP BY a.id, eu.name, a.bank_name
ORDER BY tx_count DESC;
-- Trap: COUNT(*) gives 1 for an account with no transactions (LEFT JOIN null row); COUNT(t.id) gives 0.
