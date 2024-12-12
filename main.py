import os
import subprocess
from datetime import datetime, timedelta

# Configurable variables
repo_name = "mere-aka"
commit_message = "commit - "
username = "AlzyWelzy"  # Replace with your GitHub username
email = "welzyalzy@gmail.com"  # Replace with your GitHub email
remote_url = f"https://github.com/{username}/{repo_name}.git"


# Create a new repository
def initialize_repo():
    if not os.path.exists(repo_name):
        os.makedirs(repo_name)
    os.chdir(repo_name)
    subprocess.run(["git", "init"], check=True)
    subprocess.run(["git", "config", "user.name", username], check=True)
    subprocess.run(["git", "config", "user.email", email], check=True)


# Generate fake commits
def generate_commits(days):
    start_date = datetime.now() - timedelta(days=days)
    for i in range(days):
        commit_date = start_date + timedelta(days=i)
        formatted_date = commit_date.strftime("%Y-%m-%d %H:%M:%S")

        # Create a dummy file for each commit
        file_name = f"dummy_{i}.txt"
        with open(file_name, "w") as f:
            f.write(f"Commit for {formatted_date}\n")

        subprocess.run(["git", "add", file_name], check=True)

        # Make the commit with the backdated timestamp
        env = os.environ.copy()
        env["GIT_COMMITTER_DATE"] = formatted_date
        subprocess.run(
            ["git", "commit", "--date", formatted_date, "-m", commit_message],
            check=True,
            env=env,
        )


# Push the changes to GitHub
def push_to_github():
    subprocess.run(["git", "branch", "-M", "main"], check=True)
    subprocess.run(["git", "remote", "add", "origin", remote_url], check=True)
    subprocess.run(["git", "push", "-u", "origin", "main"], check=True)


# Main script
def main():
    try:
        initialize_repo()
        generate_commits(1001)  # Generate commits for 1001 days
        push_to_github()
        print("Successfully generated and pushed fake commits!")
    except subprocess.CalledProcessError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"Unexpected error: {e}")


if __name__ == "__main__":
    main()
