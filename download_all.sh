# Create a directory to store the repositories
mkdir ~/repos
cd ~/repos

# Get the list of repositories
curl -s "https://api.github.com/users/GITHUB_USERNAME/repos?per_page=1000" |  jq '.[].name' | tr -d '"' | while read repo; do
   git clone https://github.com/GITHUB_USERNAME/$repo.git
done
