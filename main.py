"""
GitHub Commits Farm
This program farms commits on your GitHub
account for no particular reason but 
clout, fame and the fact that it just
looks cool.
"""
import os
import subprocess
import random
import time
import string
from datetime import datetime

github_username = "SelimWaly"
repository_name = "commit"
proj_dir = "D:/VSCode/GitHub Commits Farm"
os.chdir(proj_dir)

def generate_salt():
    characters = string.ascii_lowercase + string.digits + string.punctuation
    random_string = ''.join(random.choice(characters) for _ in range(20))
    return random_string

commits = 0

print(f"Running GitHub Commits Farm at Timestamp [{datetime.now().strftime('%H:%M:%S')}]...")

while True:
    print("Choosing programming language...")
    generated = random.randint(1, 10)

    if generated == 1 or generated == 2 or generated == 3:
        print("Awaiting to remove monitoring on suspicousness from GitHub servers...")
        time.sleep(15)

    elif generated == 4:
        try:
            print("Creating a commit with a C++ file...")
            file_content = """#include <iostream>

            int main() {
                std::cout << "Hello, World!" << std::endl;
                return 0;
            }
            """
            print("Generating salt...")
            salt = generate_salt()
            file_path = os.path.join(proj_dir, f"Temp-{salt}.cpp")
            with open(file_path, "w") as file:
                file.write(file_content)
            subprocess.run(["git", "init"])
            subprocess.run(["git", "add", f"Temp-{salt}.cpp"])
            subprocess.run(["git", "commit", "-m", f"Add Temp-{salt}.cpp"])
            github_repo_url = f"https://github.com/{github_username}/{repository_name}.git"
            subprocess.run(["git", "remote", "add", "origin", github_repo_url])
            subprocess.run(["git", "push", "-u", "origin", "master"])
            os.remove(file_path)
            commits+=1
            print(f"Commits: {commits}")
        except Exception as e:
            print(f"Reloading due to {e}")

    elif generated == 5:
        try:
            print("Creating a commit with a C file...")
            file_content = """#include <stdio.h>

            int main() {
                printf("Hello, world!\n");
                return 0;
            }

            """
            print("Generating salt...")
            salt = generate_salt()
            file_path = os.path.join(proj_dir, f"Temp-{salt}.c")
            with open(file_path, "w") as file:
                file.write(file_content)
            subprocess.run(["git", "init"])
            subprocess.run(["git", "add", f"Temp-{salt}.c"])
            subprocess.run(["git", "commit", "-m", f"Add Temp-{salt}.c"])
            github_repo_url = f"https://github.com/{github_username}/{repository_name}.git"
            subprocess.run(["git", "remote", "add", "origin", github_repo_url])
            subprocess.run(["git", "push", "-u", "origin", "master"])
            os.remove(file_path)
            commits+=1
            print(f"Commits: {commits}")
        except Exception as e:
            print(f"Reloading due to {e}")

    elif generated == 6:
        try:
            print("Creating a commit with a Python file...")
            file_content = """print('Hello, world!') """
            print("Generating salt...")
            salt = generate_salt()
            file_path = os.path.join(proj_dir, f"Temp-{salt}.py")
            with open(file_path, "w") as file:
                file.write(file_content)
            subprocess.run(["git", "init"])
            subprocess.run(["git", "add", f"Temp-{salt}.py"])
            subprocess.run(["git", "commit", "-m", f"Add Temp-{salt}.py"])
            github_repo_url = f"https://github.com/{github_username}/{repository_name}.git"
            subprocess.run(["git", "remote", "add", "origin", github_repo_url])
            subprocess.run(["git", "push", "-u", "origin", "master"])
            os.remove(file_path)
            commits+=1
            print(f"Commits: {commits}")
        except Exception as e:
            print(f"Reloading due to {e}")

    elif generated == 7:
        try:
            print("Creating a commit with a Jupyter file...")
            file_content = """print('Hello, world!') """
            print("Generating salt...")
            salt = generate_salt()
            file_path = os.path.join(proj_dir, f"Temp-{salt}.ipynb")
            with open(file_path, "w") as file:
                file.write(file_content)
            subprocess.run(["git", "init"])
            subprocess.run(["git", "add", f"Temp-{salt}.ipynb"])
            subprocess.run(["git", "commit", "-m", f"Add Temp-{salt}.ipynb"])
            github_repo_url = f"https://github.com/{github_username}/{repository_name}.git"
            subprocess.run(["git", "remote", "add", "origin", github_repo_url])
            subprocess.run(["git", "push", "-u", "origin", "master"])
            os.remove(file_path)
            commits+=1
            print(f"Commits: {commits}")
        except Exception as e:
            print(f"Reloading due to {e}")

    elif generated == 8:
        try:
            print("Creating a commit with a JavaScript file...")
            file_content = """console.log('Hello, world!'); """
            print("Generating salt...")
            salt = generate_salt()
            file_path = os.path.join(proj_dir, f"Temp-{salt}.js")
            with open(file_path, "w") as file:
                file.write(file_content)
            subprocess.run(["git", "init"])
            subprocess.run(["git", "add", f"Temp-{salt}.js"])
            subprocess.run(["git", "commit", "-m", f"Add Temp-{salt}.js"])
            github_repo_url = f"https://github.com/{github_username}/{repository_name}.git"
            subprocess.run(["git", "remote", "add", "origin", github_repo_url])
            subprocess.run(["git", "push", "-u", "origin", "master"])
            os.remove(file_path)
            commits+=1
            print(f"Commits: {commits}")
        except Exception as e:
            print(f"Reloading due to {e}")

    elif generated == 9:
        try:
            print("Creating a commit with a TypeScript file...")
            file_content = """console.log('Hello, world!'); """
            print("Generating salt...")
            salt = generate_salt()
            file_path = os.path.join(proj_dir, f"Temp-{salt}.ts")
            with open(file_path, "w") as file:
                file.write(file_content)
            subprocess.run(["git", "init"])
            subprocess.run(["git", "add", f"Temp-{salt}.ts"])
            subprocess.run(["git", "commit", "-m", f"Add Temp-{salt}.ts"])
            github_repo_url = f"https://github.com/{github_username}/{repository_name}.git"
            subprocess.run(["git", "remote", "add", "origin", github_repo_url])
            subprocess.run(["git", "push", "-u", "origin", "master"])
            os.remove(file_path)
            commits+=1
            print(f"Commits: {commits}")
        except Exception as e:
            print(f"Reloading due to {e}")

    else:
        try:
            print("Creating a commit with a Brainfuck file...")
            file_content = """++++++++++[>+++++++>++++++++++>+++>+<<<<-]>++.>+.+++++++..+++.>++.<<+++++++++++++.>++++.--------.++++++++++++.--------.--------.
    """
            print("Generating salt...")
            salt = generate_salt()
            file_path = os.path.join(proj_dir, f"Temp-{salt}.bf")
            with open(file_path, "w") as file:
                file.write(file_content)
            subprocess.run(["git", "init"])
            subprocess.run(["git", "add", f"Temp-{salt}.bf"])
            subprocess.run(["git", "commit", "-m", f"Add Temp-{salt}.bf"])
            github_repo_url = f"https://github.com/{github_username}/{repository_name}.git"
            subprocess.run(["git", "remote", "add", "origin", github_repo_url])
            subprocess.run(["git", "push", "-u", "origin", "master"])
            os.remove(file_path)
            commits+=1
            print(f"Commits: {commits}")
        except Exception as e:
            print(f"Reloading due to {e}")
