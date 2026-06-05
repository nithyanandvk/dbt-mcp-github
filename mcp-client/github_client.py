import os
from git import Repo
import requests
from dotenv import load_dotenv

load_dotenv()

GITHUB_TOKEN = os.getenv("GITHUB_TOKEN")

REPO_NAME = os.getenv(
    "GITHUB_REPO"
)

REPO_PATH = os.path.abspath(
    os.path.join(
        os.path.dirname(__file__),
        ".."
    )
)


def create_branch(branch_name):

    repo = Repo(REPO_PATH)

    repo.git.checkout("dev")

    repo.git.pull(
        "origin",
        "dev"
    )

    new_branch = repo.create_head(
        branch_name
    )

    new_branch.checkout()

    print(f"[GIT] Branch created: {branch_name}")


def commit_changes(message):

    repo = Repo(REPO_PATH)

    repo.git.add(A=True)

    repo.index.commit(message)

    print("[GIT] Commit successful")


def push_branch(branch_name):

    repo = Repo(REPO_PATH)

    origin = repo.remote(
        name="origin"
    )

    origin.push(
        branch_name,
        set_upstream=True
    )

    print("[GIT] Push successful")


def create_pull_request(
    branch_name,
    title,
    body=""
):

    url = f"https://api.github.com/repos/{REPO_NAME}/pulls"

    headers = {
        "Authorization": f"Bearer {GITHUB_TOKEN}",
        "Accept": "application/vnd.github+json"
    }

    payload = {
        "title": title,
        "head": branch_name,
        "base": "dev",
        "body": body
    }

    response = requests.post(
        url,
        json=payload,
        headers=headers
    )

    if response.status_code in [200, 201]:

        print(
            "[GITHUB] PR created"
        )

        return response.json()

    print(response.text)

    return None