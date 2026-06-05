import json
import re



def parse_response(response):

    if response is None:
        return {"error": "empty response"}

    if "ERROR" in response:
        return {
            "error": response
        }

    response = response.strip()

    response = re.sub(r"^```json", "", response)
    response = re.sub(r"```$", "", response)

    try:
        return json.loads(response)
    except Exception as e:
        return {
            "error": "invalid_json",
            "raw": response
        }