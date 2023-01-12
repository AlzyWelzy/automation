# Create a directory to store the repositories
mkdir ~/repos
cd ~/repos

# Get the list of repositories
curl -s "https://api.github.com/users/AlzyWelzy/repos?type=all" |  jq '.[].name' | tr -d '"' | while read repo; do
   git clone git@github.com:AlzyWelzy/$repo.git
done
