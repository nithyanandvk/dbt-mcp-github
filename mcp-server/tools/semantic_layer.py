import yaml
import os

CURRENT_DIR = os.path.dirname(os.path.abspath(__file__))

METRICS_FILE = os.path.join(
    CURRENT_DIR,
    "metrics.yaml"
)

with open(METRICS_FILE, "r", encoding="utf-8") as f:
    METRICS = yaml.safe_load(f)


def get_rule(metric):
    return METRICS.get(metric)


def get_all_rules():
    return METRICS