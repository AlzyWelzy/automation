import os
import subprocess
from datetime import datetime, timedelta

# Configurable variables
repo_path = "./hehe"  # Replace with the path to your repo
commit_message = "Backdated commit"
commit_dir = "commits"  # Directory for generated files
days_to_backdate = 1001  # Number of days for backdated commits


def generate_commits(repo_path, days_to_backdate):
    os.chdir(repo_path)
    if not os.path.exists(commit_dir):
        os.makedirs(commit_dir)

    start_date = datetime.now() - timedelta(days=days_to_backdate)
    for i in range(days_to_backdate):
        commit_date = start_date + timedelta(days=i)
        formatted_date = commit_date.strftime("%Y-%m-%d %H:%M:%S")

        # Create a dummy file in the commit directory
        file_name = os.path.join(commit_dir, f"dummy_{i}.txt")
        with open(file_name, "w") as f:
            f.write(f"Commit for {formatted_date}\\n")

        subprocess.run(["git", "add", file_name], check=True)

        # Make the commit with the backdated timestamp
        env = os.environ.copy()
        env["GIT_COMMITTER_DATE"] = formatted_date
        subprocess.run(
            ["git", "commit", "--date", formatted_date, "-m", commit_message],
            check=True,
            env=env,
        )

    # Push the changes
    subprocess.run(["git", "push"], check=True)


if __name__ == "__main__":
    generate_commits(repo_path, days_to_backdate)
