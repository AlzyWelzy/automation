import git
from github import Github, GithubException
import requests

# Get AGPL 3.0 license content from GitHub's License API
response = requests.get("https://api.github.com/licenses/agpl-3.0")
AGPL_LICENSE = response.json()["body"]


# Github access token
ACCESS_TOKEN = "ACCESS_TOKEN"

# Github username
username = "USERNAME"

# Connect to Github API
g = Github(access_token)

# Get the user
user = g.get_user(username)

# Get all the repos
repos = user.get_repos()


for repo in repos:
    # Check if a license file exists in the repo
    if repo.get_license() is not None:
        # Update the license file with AGPL 3.0 content
        repo.update_file("LICENSE", "Update license to AGPL 3.0",
                         AGPL_LICENSE, repo.get_license().sha)
    else:
        # Create a new license file with AGPL 3.0 content
        repo.create_file("LICENSE", "Add AGPL 3.0 license", AGPL_LICENSE)
    # Get the repository's local clone
    repo_name = repo.name
    clone_url = repo.clone_url
    local_path = f"/path/to/local/clone/{repo_name}"
    git.Repo.clone_from(clone_url, local_path)
    repo = git.Repo(local_path)
    repo.git.add('.')
    repo.index.commit("Update license to AGPL 3.0")
    repo.remote().push()
