#!/bin/bash

echo "Enter your Django project name:"
read project_name

echo "Cloning Django project template..."
git clone https://github.com/AlzyWelzy/django-project-template.git $project_name

# Move into the project directory
cd $project_name

# Remove the .git directory to start with a fresh repository
rm -rf .git

# Replace project_name in README.md, CONTRIBUTING.md, and CODE_OF_CONDUCT.md
sed -i '' -e "s/your_project_name/$project_name/g" README.md
sed -i '' -e "s/your_project_name/$project_name/g" CONTRIBUTING.md
sed -i '' -e "s/your_project_name/$project_name/g" CODE_OF_CONDUCT.md

# Create a virtual environment
python3 -m venv venv

# Activate the virtual environment
source venv/bin/activate

# Install project dependencies
pip install -r requirements.txt

# Initialize the database
python manage.py migrate

echo "Django project $project_name created successfully."
