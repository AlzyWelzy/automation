import os
import requests

# The GitHub account from which you want to copy the repositories
source_username = "SOURCE_USERNAME"

# Your GitHub access token
access_token = "YOUR_ACCESS_TOKEN"

# Your GitHub username
target_username = "TARGET_USERNAME"

# Get a list of all public repositories for the user
url = f"https://api.github.com/users/{source_username}/repos?per_page=1000"
headers = {
    "Authorization": f"Token {access_token}",
    "Accept": "application/vnd.github+json",
}
response = requests.get(url, headers=headers)
repos = response.json()

# Clone each repository and create a fork in the target account
for repo in repos:
    repo_name = repo["name"]
    repo_url = repo["clone_url"]
    fork_url = f"https://api.github.com/repos/{source_username}/{repo_name}/forks"
    requests.post(fork_url, headers=headers)
