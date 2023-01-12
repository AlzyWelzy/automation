# Get the GitHub username from the user
read -p "Enter the Github username:" username

# Create a directory to store the repositories
mkdir ~/repos
cd ~/repos

# Get the list of repositories
curl -s "https://api.github.com/users/$username/repos?per_page=1000" |  jq '.[].name' | tr -d '"' | while read repo; do
   git clone https://github.com/$username/$repo.git
done
