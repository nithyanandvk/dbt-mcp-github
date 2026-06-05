SELECT
    o.order_id,
    o.customer_id,
    o.product_id,
    o.quantity,
    o.order_date,

    p.product_name,
    p.unit_price,

    (o.quantity * p.unit_price) AS gross_revenue

FROM {{ ref('stg_orders') }} o
LEFT JOIN {{ ref('stg_products') }} p
    ON o.product_id = p.product_id