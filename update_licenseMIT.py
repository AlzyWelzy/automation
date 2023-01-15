import os
import requests

access_token = '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'
username = 'AlzyWelzy'

# Get MIT license content
response = requests.get(f"https://api.github.com/licenses/mit", headers={
    "Accept": "application/vnd.github+json",
    "Authorization": f"Token {access_token}"
})
mit_text = response.json()["body"]

# Get all repositories from the user
response = requests.get(f"https://api.github.com/users/{username}/repos", headers={
    "Accept": "application/vnd.github+json",
    "Authorization": f"Token {access_token}"
})
repos = response.json()

# Iterate through all repositories
for repo in repos:
    # Convert HTTPS URL to SSH URL
    ssh_url = repo['clone_url'].replace('https://', 'git@').replace('github.com/', 'github.com:')

    # Clone repository using SSH
    os.system(f"git clone {ssh_url}")

    # Go to repository directory
    os.chdir(repo["name"])

    # Check if LICENSE file already exists
    if os.path.isfile("LICENSE"):
        # Replace contents of LICENSE file with MIT license text
        with open("LICENSE", "w") as f:
            f.write(mit_text)
    else:
        # Create LICENSE file with MIT license text
        with open("LICENSE", "w") as f:
            f.write(mit_text)

    # Add and commit changes
    os.system("git add .")
    os.system('git commit -m "Added MIT license"')

    # Push changes to GitHub
    os.system("git push")

    # Go back to parent directory
    os.chdir("..")
