import requests
import zipfile
import io

# GitHub username
username = "GITHUB_USERNAME"

# GitHub REST API endpoint for getting a user's repositories
url = f"https://api.github.com/users/{username}/repos"

# Make the API call
response = requests.get(url)

# Get the repository data from the response
repositories = response.json()

# Iterate through the repositories
for repo in repositories:
    # Get the repository name and download URL
    repo_name = repo["name"]
    download_url = repo["zip_url"]
    
    # Download the repository as a zip file
    repo_zip = requests.get(download_url)
    with zipfile.ZipFile(io.BytesIO(repo_zip.content)) as zip_file:
        zip_file.extractall(repo_name)

print(f"All public repositories of {username} have been downloaded.")
