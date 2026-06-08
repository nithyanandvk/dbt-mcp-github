import requests

def get_context(user_request: str):
    try:
        response = requests.post(
            "http://localhost:8000/context",
            json={"user_request": user_request},
            timeout=60
        )

        if response.status_code != 200:
            print("[ERROR] Context API failed")
            print(response.text)
            return None

        try:
            return response.json()
        except Exception:
            print("[ERROR] Invalid JSON from server:")
            print(response.text)
            return None

    except Exception as e:
        print("[ERROR] Request failed:", str(e))
        return None

def apply_ai_change(model_name: str, new_sql: str):
    try:
        response = requests.post(
            "http://localhost:8000/apply-ai-change",
            json={
                "model_name": model_name,
                "sql": new_sql
            },
            timeout=60
        )

        if response.status_code != 200:
            print("[ERROR] Patch failed")
            print(response.text)
            return None

        try:
            return response.json()
        except Exception:
            print("[ERROR] Invalid patch response")
            print(response.text)
            return None

    except Exception as e:
        print("[ERROR] Patch request failed:", str(e))
        return None