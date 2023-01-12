import os
import requests

# Your GitHub access token
access_token = "YOUR_ACCESS_TOKEN"

# Your GitHub username
username = "YOUR_USERNAME"

# Get a copy of the AGPL-3.0 license
agpl_license_url = "https://api.github.com/licenses/agpl-3.0"
headers = {
    "Authorization": f"Token {access_token}",
    "Accept": "application/vnd.github+json",
}
response = requests.get(agpl_license_url, headers=headers)
agpl_license_text = response.json()["body"]

# Get a list of all repositories for the user, including private ones
url = f"https://api.github.com/user/repos?per_page=1000"
headers["Authorization"] = f"Token {access_token}"
response = requests.get(url, headers=headers)
repos = response.json()

# Download each repository and change the license
for repo in repos:
    repo_name = repo["name"]
    repo_url = repo["clone_url"]
    os.system(f"git clone {repo_url}")
    os.chdir(repo_name)
    default_branch = requests.get(repo["branches_url"].replace("{/branch}","")).json()[0]["name"]
    with open("LICENSE", "w") as f:
        f.write(agpl_license_text)
    os.system("git add LICENSE")
    os.system('git commit -m "Changing license to AGPL-3.0"')
    os.system(f"git push origin {default_branch}")
    os.chdir("..")
