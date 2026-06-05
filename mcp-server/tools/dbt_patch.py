import os


def get_model_path(model_name: str):

    base = os.path.abspath(
        os.path.join(
            os.path.dirname(__file__),
            "..",
            "..",
            "dbt_project",
            "models"
        )
    )

    for root, _, files in os.walk(base):

        for file in files:

            if file == f"{model_name}.sql":

                return os.path.join(root, file)

    return None


def apply_patch(model_name: str, new_sql: str):

    path = get_model_path(model_name)

    if not path:
        return {
            "status": "error",
            "message": f"Model {model_name} not found"
        }

    with open(path, "w", encoding="utf-8") as f:
        f.write(new_sql)

    return {
        "status": "success",
        "model": model_name,
        "file": path
    }