CREATE DATABASE dbt_demo;
GO

USE dbt_demo;
GO


CREATE TABLE orders (
    order_id INT,
    customer_id INT,
    product_id INT,
    quantity INT,
    order_date DATE
);

CREATE TABLE products (
    product_id INT,
    product_name VARCHAR(100),
    unit_price DECIMAL(10,2)
);

CREATE TABLE refunds (
    refund_id INT,
    order_id INT,
    refunded_amount DECIMAL(10,2),
    refund_date DATE
);

CREATE TABLE customers (
    customer_id INT,
    customer_name VARCHAR(100),
    region VARCHAR(50)
);

INSERT INTO customers VALUES
(1,'John','East'),
(2,'Alice','West'),
(3,'Bob','South'),
(4,'David','North'),
(5,'Emma','East');

INSERT INTO products VALUES
(101,'Laptop',50000),
(102,'Mouse',1000),
(103,'Keyboard',2500),
(104,'Monitor',12000),
(105,'Headset',3000);

INSERT INTO orders VALUES
(1001,1,101,1,'2026-01-01'),
(1002,1,102,2,'2026-01-02'),
(1003,2,104,1,'2026-01-03'),
(1004,3,105,3,'2026-01-04'),
(1005,4,103,2,'2026-01-05'),
(1006,5,101,1,'2026-01-06'),
(1007,2,102,5,'2026-01-07');


INSERT INTO refunds VALUES
(1,1002,500,'2026-01-10'),
(2,1004,1000,'2026-01-11');

SELECT * FROM customers;
SELECT * FROM products;
SELECT * FROM orders;
SELECT * FROM refunds;