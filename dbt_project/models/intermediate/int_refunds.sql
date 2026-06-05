SELECT
    order_id,
    SUM(refunded_amount) AS total_refund
FROM {{ ref('stg_refunds') }}
GROUP BY order_id