import sys
import os
import shutil

from gitbook2mkdocs.plugin import Gitbook2Mkdocs

# Get path from args
repo_path:str
try:
    repo_path = sys.argv[1]
except IndexError:
    print("Usage: python migrateGitbook.py <path_to_repository>")
    repo_path = "../docs/de/Siedler-4/"
    #sys.exit(1)

if not os.path.isdir(repo_path):
    print(f"Invalid path: {repo_path}. Set the correct path to the repository.")
    sys.exit(1)

# Get all .md files in all folders and subfolders in the repo
repo_files = []
for root, dirs, files in os.walk(repo_path):
    for file in files:
        if file.endswith(".md"):
            repo_files.append(os.path.join(root, file))

migrator = Gitbook2Mkdocs()
for f in repo_files:
    new_content: str
    with open(f, "r", encoding="utf-8") as file:
        content = file.read()
        new_content = migrator.on_page_markdown(content, None, None, None)

    with open(f, "w", encoding="utf-8") as file:
        file.write(new_content)


# Move actual folder from .gitbook/assets/ to /assets/
if os.path.exists(os.path.join(repo_path, ".gitbook", "assets")):
    shutil.move(os.path.join(repo_path, ".gitbook", "assets"), os.path.join(repo_path, "assets"))
