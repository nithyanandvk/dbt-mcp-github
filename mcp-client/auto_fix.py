from ai_client import get_context
from prompt_builder import build_prompt
from llm_client import ask_llm
from response_parser import parse_response

import requests


def auto_fix(user_request):

    context = get_context(user_request)

    prompt = build_prompt(context)

    response = ask_llm(prompt)

    result = parse_response(response)

    if result["implemented"]:

        return {
            "status": "already implemented"
        }

    requests.post(
        "http://localhost:8000/dbt/patch",
        json={
            "model_name": result["target_model"],
            "new_sql": result["sql"]
        }
    )

    return result