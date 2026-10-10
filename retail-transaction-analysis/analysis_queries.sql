


SELECT
    store_location,
    ROUND(SUM(price), 2) AS total_sales,
    COUNT(receipt_id) AS total_transactions
FROM transactions
GROUP BY store_location
ORDER BY total_sales DESC;


-- 2. Analyze payment methods

SELECT
    payment_method,
    COUNT(receipt_id) AS total_transactions,
    ROUND(AVG(price), 2) AS average_transaction_value
FROM transactions
GROUP BY payment_method
ORDER BY total_transactions DESC;

-- 3. Highest transaction price in each city

SELECT
    store_location,
    MAX(price) AS highest_transaction
FROM transactions
GROUP BY store_location
ORDER BY highest_transaction DESC;

-- 4. Transaction count by product category

SELECT
    item_category,
    COUNT(receipt_id) AS total_transactions,
    ROUND(SUM(price), 2) AS total_sales
FROM transactions
GROUP BY item_category
ORDER BY total_sales DESC;


-- 5. Cities with total sales greater than 1000

SELECT
    store_location,
    ROUND(SUM(price), 2) AS total_sales
FROM transactions
GROUP BY store_location
HAVING SUM(price) > 1000
ORDER BY total_sales DESC;

-- 6. Transactions above the average price

SELECT
    receipt_id,
    store_location,
    item_category,
    price
FROM transactions
WHERE price > (
    SELECT AVG(price)
    FROM transactions
)
ORDER BY price DESC;

-- 7. Daily sales analysis

SELECT
    DATE(timestamp) AS transaction_date,
    ROUND(SUM(price), 2) AS daily_sales,
    COUNT(receipt_id) AS total_transactions
FROM transactions
GROUP BY DATE(timestamp)
ORDER BY transaction_date;

-- 8. Sales by city and product category

SELECT
    store_location,
    item_category,
    ROUND(SUM(price), 2) AS total_sales,
    COUNT(receipt_id) AS total_transactions
FROM transactions
GROUP BY store_location, item_category
ORDER BY store_location, total_sales DESC;

-- 9. Identify possible duplicate records

SELECT
    store_location,
    item_category,
    price,
    payment_method,
    timestamp,
    COUNT(*) AS duplicate_count
FROM transactions
GROUP BY
    store_location,
    item_category,
    price,
    payment_method,
    timestamp
HAVING COUNT(*) > 1;

-- 10. Rank cities by total sales

SELECT
    store_location,
    ROUND(SUM(price), 2) AS total_sales,
    RANK() OVER (ORDER BY SUM(price) DESC) AS sales_rank
FROM transactions
GROUP BY store_location
ORDER BY sales_rank;
