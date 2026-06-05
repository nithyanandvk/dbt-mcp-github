import subprocess
import os

def run_dbt(command="run"):
    """
    Executes dbt commands safely and returns result
    """

    project_dir = os.path.abspath(
        os.path.join(os.path.dirname(__file__), "..", "..", "dbt_project")
    )

    cmd = ["dbt", command]

    try:
        process = subprocess.run(
            cmd,
            cwd=project_dir,
            capture_output=True,
            text=True
        )

        return {
            "command": " ".join(cmd),
            "return_code": process.returncode,
            "stdout": process.stdout,
            "stderr": process.stderr,
            "status": "success" if process.returncode == 0 else "failed"
        }

    except Exception as e:
        return {
            "status": "error",
            "error": str(e)
        }


def run_dbt_tests():
    return run_dbt("test")