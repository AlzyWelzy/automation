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

# Define the MIT license key
MIT_LICENSE_KEY = "mit"
# MIT_LICENSE_KEY = "agpl-3.0"

# Get the MIT license content from the GitHub license API
url = f"https://api.github.com/licenses/{MIT_LICENSE_KEY}"
mit_license = session.get(url).json()
MIT_LICENSE = mit_license["body"]

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
            f.write(MIT_LICENSE)
    else:
        with open(license_path, "w") as f:
            f.write(MIT_LICENSE)
    repo.git.add('.')
    repo.index.commit("Update license to MIT")
    origin = repo.remote(name='origin')
    origin.set_url(
        f"https://{ACCESS_TOKEN}@github.com/{username}/{repo_name}.git")
    origin.push()
