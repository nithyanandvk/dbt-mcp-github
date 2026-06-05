from llm_client import ask_llm
from prompt_builder import build_prompt
from ai_client import get_context
from response_parser import parse_response
from ai_client import apply_ai_change
from github_client import (
    create_branch,
    commit_changes,
    push_branch,
    create_pull_request
)
import time

context = get_context("add average refund per order")

prompt = build_prompt(context)

print("========== PROMPT ==========")
print(prompt)

response = ask_llm(prompt)

print("\n========== GEMINI RESPONSE ==========")
print(response)

result = parse_response(response)
from ai_client import apply_ai_change
from ai_client import apply_ai_change

print("\n========== ANALYSIS ==========")
print("Target Model:", result["target_model"])
print("Metric Exists:", result["metric_exists"])
print("Implemented:", result["implemented"])

if not result["implemented"]:

    print("\n[INFO] AI generated SQL change")
    
    print("[INFO] Applying patch...")

    outcome = apply_ai_change(
        result["target_model"],
        result["sql"]
    )

    if not outcome:
        print("[FAIL] Patch failed")
        exit(1)

    print("[SUCCESS] Patch applied:", outcome)

    print("\n========== APPLY RESULT ==========")

    if outcome["status"] == "success":
        print(" SQL replaced successfully")
        print(" dbt run successful")
        print(" dbt test successful")
        print(f" Model updated: {result['target_model']}")

        print("\n[INFO] Starting GitHub workflow...")

        branch_name = (
            f"ai/{result['target_model']}-{int(time.time())}"
        )

        create_branch(branch_name)

        commit_changes("AI: update dbt model via MCP pipeline")

        push_branch(branch_name)

        pr = create_pull_request(
            branch_name=branch_name,
            title="AI: Automated dbt model update",
            body="Generated via MCP + Gemini pipeline"
        )
        print("PR OBJECT:", pr)
        print("\n========== FINAL RESULT ==========")
        print("Branch:", branch_name)
        print("PR:", pr["html_url"] if pr else "FAILED")

    elif outcome["status"] == "dbt_run_failed":
        print(" SQL replaced")
        print("dbt run failed")
        print(outcome["details"]["stderr"])

    elif outcome["status"] == "dbt_test_failed":
        print(" SQL replaced")
        print(" dbt run successful")
        print("dbt test failed")
        print(outcome["details"]["stderr"])

    else:
        print("Error")
        print(outcome)
    
    

else:

    print("\n Metric already implemented")
    print("No code change required")