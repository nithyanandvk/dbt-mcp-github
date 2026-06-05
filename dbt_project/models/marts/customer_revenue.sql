WITH orders AS (
    SELECT * FROM {{ ref('int_orders_enriched') }}
),

refunds AS (
    SELECT * FROM {{ ref('int_refunds') }}
)

SELECT
    o.customer_id,

    SUM(o.gross_revenue) AS total_revenue,
    COALESCE(SUM(r.total_refund), 0) AS total_refund,

    SUM(o.gross_revenue) - COALESCE(SUM(r.total_refund), 0) AS net_revenue,

    COUNT(DISTINCT o.order_id) AS total_orders,

    (SUM(o.gross_revenue) / COUNT(DISTINCT o.order_id)) AS avg_order_value

FROM orders o
LEFT JOIN refunds r
    ON o.order_id = r.order_id

GROUP BY o.customer_id