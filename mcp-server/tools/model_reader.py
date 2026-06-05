import os


def get_all_model_sql():

    models_dir = os.path.abspath(
        os.path.join(
            os.path.dirname(__file__),
            "..",
            "..",
            "dbt_project",
            "models"
        )
    )

    sql_models = {}

    for root, _, files in os.walk(models_dir):

        for file in files:

            if file.endswith(".sql"):

                path = os.path.join(root, file)

                with open(path, "r", encoding="utf-8") as f:

                    sql_models[file.replace(".sql", "")] = f.read()

    return sql_models