import json


def build_prompt(context):

    return f"""
You are a Principal Analytics Engineer.

USER REQUEST

{context["user_request"]}


DBT Metadata + SQL:
{json.dumps(context["models"], indent=2)}

Business Metrics:
{json.dumps(context["semantic_rules"], indent=2)}

Instructions:

1. Analyze the user request.
2. Analyze model lineage.
3. Analyze semantic metrics.
4. Analyze existing SQL implementations.
5. Determine whether the requested column already exists.
6. Identify the correct target model.
7. If the model SQL is incomplete or incorrect, generate a full replacement SQL.
8. Use existing metrics whenever possible.
9. Do not modify unrelated models.



IMPORTANT

Determine:

1. metric_exists
2. implemented

Definitions:

metric_exists:
- metric already exists in metadata OR semantic layer

implemented:
- current SQL actually calculates the metric

Rules:

IF metric_exists = true
AND implemented = true

THEN:
- sql=""

IF metric_exists = true
AND implemented = false

THEN:
- generate complete replacement SQL

IF metric_exists = false

THEN:
- generate complete replacement SQL

Always return valid JSON only.



    
RETURN JSON ONLY



{{
  "target_model": "",
  "reasoning": "",
  "metric_exists": false,
  "implemented": false,
  "sql": ""
}}
"""