import subprocess

# Get the GitHub username from the user
username = input("Enter the Github username:")

# Create a directory to store the repositories
subprocess.run(["mkdir", "-p", "~/repos"])
subprocess.run(["cd", "~/repos"])

# Use the git clone command to clone all repositories from a user's account
subprocess.run(["git", "clone", "git@github.com:"+username+"/repo_name.git"])
