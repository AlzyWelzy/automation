import os
import git
import requests

# Github access token
# ACCESS_TOKEN = ""
ACCESS_TOKEN = input("Enter the ACCESS TOKEN: ")

# Github username
# username = ""
username = input("Enter Username: ")

# Connect to the GitHub API using an access token
session = requests.Session()
session.auth = (ACCESS_TOKEN, "")

# Get the user's repositories
url = f"https://api.github.com/users/{username}/repos"
repos = session.get(url).json()

# Define the MIT license key
license_key = input("Enter the license key: ")

# Get the license content from the GitHub license API
url = f"https://api.github.com/licenses/{license_key}"
license = session.get(url).json()
license_content = license["body"]

for repo in repos:
    repo_name = repo["name"]
    clone_url = repo["clone_url"]
    local_path = f"{os.getcwd()}/{repo_name}"
    try:
        git.Repo.clone_from(clone_url, local_path)
        repo = git.Repo(local_path)
        # Check if a license file exists in the repo
        license_path = os.path.join(local_path, "LICENSE")
        if os.path.isfile(license_path):
            with open(license_path, "w") as f:
                f.write(license_content)
        else:
            with open(license_path, "w") as f:
                f.write(license_content)
        repo.git.add('.')
        repo.index.commit("Update license")
        origin = repo.remote(name='origin')
        origin.set_url(
            f"https://{ACCESS_TOKEN}@github.com/{username}/{repo_name}.git")
        origin.push()
    except Exception as e:
        print(f"An error occurred while processing {repo_name}")
        print(e)
