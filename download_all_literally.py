import requests
import zipfile
import io

# GitHub access token
access_token = "YOUR_ACCESS_TOKEN"

# GitHub username
username = "GITHUB_USERNAME"

# GitHub REST API endpoint for getting a user's repositories
url = f"https://api.github.com/users/{username}/repos?type=all"

# Headers for the API call, including the access token
headers = {
    "Authorization": f"Token {access_token}",
    "Accept": "application/vnd.github+json",
}

# Make the API call
response = requests.get(url, headers=headers)

# Get the repository data from the response
repositories = response.json()

# Iterate through the repositories
for repo in repositories:
    # Get the repository name and download URL
    repo_name = repo["name"]
    download_url = repo["zip_url"]

    # Download the repository as a zip file
    repo_zip = requests.get(download_url, headers=headers)
    with zipfile.ZipFile(io.BytesIO(repo_zip.content)) as zip_file:
        zip_file.extractall(repo_name)

print(f"All repositories of {username} have been downloaded.")
