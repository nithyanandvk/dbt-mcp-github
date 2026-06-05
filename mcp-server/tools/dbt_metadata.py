import json
import os

def get_path(filename):
    current_dir = os.path.dirname(os.path.abspath(__file__))
    project_root = os.path.abspath(os.path.join(current_dir, "..", ".."))
    return os.path.join(project_root, "dbt_project", "target", filename)


def load_json(path):
    if not os.path.exists(path):
        return None
    with open(path, "r", encoding="utf-8") as f:
        return json.load(f)


def list_models():

    manifest = load_json(get_path("manifest.json"))
    catalog = load_json(get_path("catalog.json"))

    if not manifest:
        raise Exception("manifest.json not found. Run dbt run")

    models = {}

    nodes = manifest.get("nodes", {})

    for node_id, node in nodes.items():

        if node.get("resource_type") != "model":
            continue

        model_name = node["name"]

        # base structure from manifest
        models[model_name] = {
            "unique_id": node_id,
            "depends_on": node.get("depends_on", {}).get("nodes", []),
            "columns": {}
        }

        # enrich from catalog.json
        if catalog and "nodes" in catalog:
            catalog_node = catalog["nodes"].get(node_id)

            if catalog_node:
                cols = catalog_node.get("columns", {})

                models[model_name]["columns"] = {
                    col: {
                        "type": cols[col].get("type"),
                        "description": cols[col].get("comment")
                    }
                    for col in cols
                }

    return models

import os

def get_models_directory():

    return os.path.abspath(
        os.path.join(
            os.path.dirname(__file__),
            "..",
            "..",
            "dbt_project",
            "models"
        )
    )

import os

def get_model_sql(model_name):

    models_dir = os.path.abspath(
        os.path.join(
            os.path.dirname(__file__),
            "..",
            "..",
            "dbt_project",
            "models"
        )
    )

    for root, _, files in os.walk(models_dir):

        for file in files:

            if file == f"{model_name}.sql":

                path = os.path.join(root, file)

                with open(path, "r", encoding="utf-8") as f:
                    return f.read()

    return ""