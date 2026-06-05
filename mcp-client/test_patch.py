import requests

response = requests.post(
    "http://localhost:8000/dbt/patch",
    json={
        "model_name": "customer_revenue",
        "new_sql": """
select
    1 as test_column
"""
    }
)

print(response.json())