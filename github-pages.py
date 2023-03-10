import os


def delete_dist_lines():
    with open('.gitignore', 'r') as gitignorefile:
        lines = gitignorefile.readlines()
    with open('.gitignore', 'w') as gitignorefile:
        for line in lines:
            if "dist" not in line and "dist-ssr" not in line:
                gitignorefile.write(line)


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

# Check for presence of package.json file
if os.path.exists("package.json"):
    # Build with npm
    print("Running npm build to build to ./dist")
    os.system("npm run build")
    delete_dist_lines()
    # Commit and push

print("github actions")
os.system('git add .')
os.system(f'git commit -m "{commit_message}"')
os.system("git subtree push --prefix dist origin gh-pages")
os.system("git push origin master")
