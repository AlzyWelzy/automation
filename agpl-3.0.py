import os
import git
import requests

# Github access token
ACCESS_TOKEN = "ACCESS_TOKEN"

# Github username
username = "USERNAME"

# Connect to the GitHub API using an access token
session = requests.Session()
session.auth = (ACCESS_TOKEN, "")

# Get the user's repositories
url = f"https://api.github.com/users/{username}/repos"
repos = session.get(url).json()

# Define the AGPL 3.0 license key
AGPL_LICENSE_KEY = "agpl-3.0"

# Get the AGPL 3.0 license content from the GitHub license API
url = f"https://api.github.com/licenses/{AGPL_LICENSE_KEY}"
agpl_license = session.get(url).json()
AGPL_LICENSE = agpl_license["body"]

for repo in repos:
    repo_name = repo["name"]
    clone_url = repo["clone_url"]
    local_path = f"{os.getcwd()}/{repo_name}"
    git.Repo.clone_from(clone_url, local_path)
    repo = git.Repo(local_path)
    # Check if a license file exists in the repo
    license_path = os.path.join(local_path, "LICENSE")
    if os.path.isfile(license_path):
        with open(license_path, "w") as f:
            f.write(AGPL_LICENSE)
    else:
        with open(license_path, "w") as f:
            f.write(AGPL_LICENSE)
    repo.git.add('.')
    repo.index.commit("Update license to AGPL 3.0")
    origin = repo.remote(name='origin')
    origin.set_url(
        f"https://{ACCESS_TOKEN}@github.com/{username}/{repo_name}.git")
    origin.push()
