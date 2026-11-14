-- Task: Count accounts in Low Salary (<20000), Average Salary (20000-50000
-- inclusive), and High Salary (>50000), including categories with no accounts.
SELECT -- Build the low-salary category row.
    'Low Salary' AS category, -- Label incomes below 20000.
    COUNT(*) AS accounts_count -- Return zero even when no accounts match.
FROM Accounts -- Read all bank accounts.
WHERE income < 20000 -- Select only low-salary accounts.
UNION ALL -- Append the next category without removing any rows.
SELECT -- Build the average-salary category row.
    'Average Salary' AS category, -- Label the middle income range.
    COUNT(*) AS accounts_count -- Count matching accounts, including zero.
FROM Accounts -- Read all bank accounts again for this category.
WHERE income BETWEEN 20000 AND 50000 -- Include both boundary values.
UNION ALL -- Append the final category row.
SELECT -- Build the high-salary category row.
    'High Salary' AS category, -- Label incomes above 50000.
    COUNT(*) AS accounts_count -- Count matching accounts, including zero.
FROM Accounts -- Read all bank accounts for the high-salary category.
WHERE income > 50000; -- Select only high-salary accounts.
