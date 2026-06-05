from tools.dbt_metadata import (
    list_models,
    get_model_sql
)

from tools.semantic_layer import get_all_rules


def build_context(user_request):

    models = list_models()

    for model_name in models:
        models[model_name]["sql"] = get_model_sql(
            model_name
        )

    return {
        "user_request": user_request,
        "models": models,
        "semantic_rules": get_all_rules()
    }