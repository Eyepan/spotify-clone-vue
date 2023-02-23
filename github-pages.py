import os

# Check if current directory is a Git repository
if not os.path.exists(".git"):
    print("Initializing Git repository...")
    os.system("git init")
    os.system("git add .")

# Prompt user to attach to remote repository if not already attached
status = os.system("git remote -v")
if status != 0:
    repo_name = input("Enter the URL of the remote repository: ")
    os.system(f"git remote add origin {repo_name}")

# Prompt user for commit message
commit_message = input("Enter a commit message: ")

# Prompt user for push type
push_type = input(
    "Enter 'master' to push to master branch or 'gh-pages' to push to gh-pages branch: ")

# Check for presence of package.json file
if os.path.exists("package.json"):
    # Build with npm
    print("Running npm build to build to ./dist")
    os.system("npm run build")

# Commit and push
print("github actions")
os.system(f'git add .')
os.system(f'git commit -m "{commit_message}"')
if push_type == "master":
    os.system("git push origin master")
else:
    os.system("git subtree push --prefix dist origin gh-pages")
