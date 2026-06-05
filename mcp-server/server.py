from fastapi import FastAPI
from pydantic import BaseModel


from tools.dbt_metadata import list_models
from tools.semantic_layer import get_rule
from tools.dbt_runner import run_dbt, run_dbt_tests
from tools.dbt_patch import apply_patch
from tools.context_builder import build_context
from tools.dbt_patch import apply_patch
from tools.dbt_runner import run_dbt, run_dbt_tests



app = FastAPI(title="DBT MCP Server")

# HEALTH
@app.get("/")
def health():
    return {"status": "MCP Server Running"}


# TOOLS
@app.get("/tools")
def tools():
    return {
        "available_tools": [
            "list_models",
            "semantic_lookup",
            "run_dbt",
            "run_dbt_tests",
            "apply_patch",
            "auto_fix"
        ]
    }


# METADATA LAYER
@app.get("/models")
def models():
    return list_models()


# SEMANTIC LAYER
@app.get("/semantic/{metric}")
def semantic(metric: str):
    rule = get_rule(metric)

    if not rule:
        return {"error": "No semantic rule found"}

    return rule


# DBT EXECUTION LAYER
@app.get("/dbt/run")
def dbt_run():
    return run_dbt("run")


@app.get("/dbt/test")
def dbt_test():
    return run_dbt_tests()


# PATCH ENGINE
class PatchRequest(BaseModel):
    model_name: str
    new_sql: str


@app.post("/dbt/patch")
def patch_model(request: PatchRequest):
    return apply_patch(request.model_name, request.new_sql)

class ContextRequest(BaseModel):
    user_request: str


@app.post("/context")
def create_context(request: ContextRequest):

    return build_context(
        request.user_request
    )

class AIChangeRequest(BaseModel):
    model_name: str
    sql: str


@app.post("/apply-ai-change")
def apply_ai_change(request: AIChangeRequest):

    patch_result = apply_patch(
        request.model_name,
        request.sql
    )

    if patch_result["status"] != "success":
        return patch_result

    run_result = run_dbt("run")

    if run_result["status"] != "success":
        return {
            "status": "dbt_run_failed",
            "details": run_result
        }

    test_result = run_dbt_tests()

    if test_result["status"] != "success":
        return {
            "status": "dbt_test_failed",
            "details": test_result
        }

    return {
        "status": "success",
        "model": request.model_name
    }