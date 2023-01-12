import os
import subprocess
import json
import requests

# Get the GitHub username from the user
username = input("Enter the Github username:")

# Get the GitHub access token from the user
token = input("Enter the Github token(If you don't have one, leave it empty):")

# Check if the user entered a token
if token:
    auth = {"Authorization": f"Token {token}"}
    url = f"https://api.github.com/users/{username}/repos"
    repos = requests.get(url, headers=auth)
    repos = json.loads(repos.text)
    repos = [repo['name'] for repo in repos]
else:
    repos = []
    url = f"https://api.github.com/users/{username}/repos"
    repos_response = requests.get(url)
    repos_json = json.loads(repos_response.text)
    for repo in repos_json:
        if repo["private"] == False:
            repos.append(repo["name"])

if repos:
    method = input(
        "Do you want to download the repos using API or ssh way? (api/ssh):")

    if method == "ssh":
        # Check if git is installed
        try:
            subprocess.run(["git", "--version"], check=True)
        except subprocess.CalledProcessError:
            git_install = input(
                "Git is not installed. Do you want to download using API? (yes/no):")
            if git_install == "yes":
                method = "api"
            else:
                print("Exiting the script.")
                exit()

        if method == "ssh":
            os.makedirs("~/repos", exist_ok=True)
            os.chdir("~/repos")
            for repo in repos:
                subprocess.run(
                    ["git", "clone", "git@github.com:"+username+"/"+repo+".git"])
            print(f"All repositories of {username} have been cloned.")

    if method == "api":
        download_all = input(
            "Do you want to download all repositories? (yes/no):")
        if download_all == "no":
            print("List of repositories:")
            for i, repo in enumerate(repos):
                print(f"{i+1}. {repo}")
            repos_to_download = input(
                "Enter the numbers of the repositories you want to download separated by a space:").split()
            repos_to_download = [repos[int(repo)-1]
                                 for repo in repos_to_download]
        else:
            repos_to_download = repos

        os.makedirs("~/repos", exist_ok=True)
        os.chdir("~/repos")
        for repo in repos_to_download:
            url = f"https://github.com/{username}/{repo}/archive/master.zip"
            response = requests.get(url)
            open(f"{repo}.zip", "wb").write(response.content)
            subprocess.
