import os
import subprocess
import json

# Ask the GitHub username
username = input("Enter the GitHub username:")

# Ask for the GitHub token
token = input("Enter the GitHub token (leave blank for public repos only):")

# Ask the user if they want to download repos using the API or SSH
method = input(
    "Enter 'API' to download repos using the API or 'SSH' to download repos using SSH:")

# If the user selected the API method
if method.upper() == "API":
    # Ask the user if they want to download all repos or just some
    download_type = input(
        "Enter 'ALL' to download all repos or 'SOME' to download specific repos:")

    # If the user selected to download all repos
    if download_type.upper() == "ALL":
        # Get the list of all repositories
        if token:
            repos = json.loads(subprocess.run(
                ["curl", "-s", f"https://api.github.com/users/{username}/repos?per_page=1000", "-H", f"Authorization: token {token}"], capture_output=True).stdout)
        else:
            repos = json.loads(subprocess.run(
                ["curl", "-s", f"https://api.github.com/users/{username}/repos?per_page=1000"], capture_output=True).stdout)
        for repo in repos:
            # Download the repository
            os.system(f"curl -LJO {repo['zipball_url']}")
    # If the user selected to download specific repos
    elif download_type.upper() == "SOME":
        # Get the list of repositories
        if token:
            repos = json.loads(subprocess.run(
                ["curl", "-s", f"https://api.github.com/users/{username}/repos?per_page=1000", "-H", f"Authorization: token {token}"], capture_output=True).stdout)
        else:
            repos = json.loads(subprocess.run(
                ["curl", "-s", f"https://api.github.com/users/{username}/repos?per_page=1000"], capture_output=True).stdout)
        # Print the list of repositories
        for i, repo in enumerate(repos):
            print(f"{i+1}. {repo['name']}")
        # Ask the user to select the repos to download
        selected_repos = input(
            "Enter the number of the repos you want to download (separated by spaces):").split(" ")
        for repo_num in selected_repos:
            # Download the selected repository
            os.system(f"curl -LJO {repos[int(repo_num)-1]['zipball_url']}")
    # If the user entered an invalid option
    else:
        print("Invalid option. Please enter 'ALL' or 'SOME'.")

# If the user selected the SSH method
elif method.upper() == "SSH":
    # Check if git is installed
    try:
        subprocess.run(["git", "--version"], check=True)
    except subprocess.CalledProcessError:
        git_installed = False
    else:
        git_installed = True

    # If git is installed
    if git_installed:
        # Create a directory to store the repositories
        os.makedirs("~/repos", exist_ok=True)
        os.chdir("~/repos")

        # Ask the user if they want to clone all repos or just some
        download_type = input(
            "Enter 'ALL' to clone all repos or 'SOME' to clone specific repos:")

        # If the user selected to clone all repos
        if download_type.upper() == "ALL":
            # Use the git clone command to clone all repositories from a user's account
            for repo in json.loads(subprocess.run(["curl", "-s", f"https://api.github.com/users/{username}/repos?per_page=1000", "-H", f"Authorization: token {token}"], capture_output=True).stdout):
                subprocess.run(
                    ["git", "clone", "git@github.com:{username}/{repo['name']}.git"])
        # # If the user selected to clone specific repos
        # elif download_type.upper() == "SOME":
        #     # Get the list of

        # If the user selected to clone specific repos
        elif download_type.upper() == "SOME":
            # Get the list of repositories
            if token:
                repos = json.loads(subprocess.run(
                    ["curl", "-s", f"https://api.github.com/users/{username}/repos?per_page=1000", "-H", f"Authorization: token {token}"], capture_output=True).stdout)
            else:
                repos = json.loads(subprocess.run(
                    ["curl", "-s", f"https://api.github.com/users/{username}/repos?per_page=1000"], capture_output=True).stdout)
            # Print the list of repositories
            for i, repo in enumerate(repos):
                print(f"{i+1}. {repo['name']}")
            # Ask the user to select the repos to clone
            selected_repos = input(
                "Enter the number of the repos you want to clone (separated by spaces):").split(" ")
            for repo_num in selected_repos:
                # Clone the selected repository
                subprocess.run(
                    ["git", "clone", "git@github.com:{username}/{repos[int(repo_num)-1]['name']}.git"])
    else:
        print("Git is not installed on your system, please install git or download the repos using API method")
