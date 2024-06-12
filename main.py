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

def get_valid_input(prompt):
    while True:
        user_input = input(prompt).strip()
        if user_input:
            return user_input
        print("Input cannot be empty or whitespace. Please try again.")

def get_project_directory():
    while True:
        proj_dir = input("Enter the directory to operate in: ").replace("/", "\\").strip()
        if proj_dir:
            if not os.path.exists(proj_dir):
                try:
                    os.makedirs(proj_dir)
                    print(f"Directory '{proj_dir}' created.")
                except OSError as e:
                    print(f"Error creating directory: {e}")
                    continue
            return proj_dir
        print("Input cannot be empty or whitespace. Please try again.")

github_username = get_valid_input("Enter your GitHub username: ")
user_name = get_valid_input("Enter your name: ")
user_email = get_valid_input("Enter your email: ")

# Set Git configuration
subprocess.run(["git", "config", "--global", "user.name", user_name], check=True)
subprocess.run(["git", "config", "--global", "user.email", user_email], check=True)

repository_name = get_valid_input("Enter your GitHub repository name: ")
proj_dir = get_project_directory()

os.chdir(proj_dir)

def generate_salt():
    characters = string.ascii_lowercase + string.digits
    random_string = ''.join(random.choice(characters) for _ in range(20))
    return random_string

commits = 0

print(f"Running GitHub Commits Farm at Timestamp [{datetime.now().strftime('%H:%M:%S')}]...")

while True:
    print("Choosing programming language...")
    generated = random.randint(1, 10)

    if generated == 1 or generated == 2:
        print("Awaiting to remove monitoring on suspiciousness from GitHub servers...")
        time.sleep(10)

    else:
        try:
            file_content = ""
            file_extension = ""
            
            if generated == 3:
                print("Creating a commit with a Dart file...")
                file_content = """void main() {
  print('Hello world!');
}

"""
                file_extension = "dart"
                
            elif generated == 4:
                print("Creating a commit with a C++ file...")
                file_content = """#include <iostream>

int main() {
    std::cout << "Hello, World!" << std::endl;
    return 0;
}
"""
                file_extension = "cpp"
            elif generated == 5:
                print("Creating a commit with a C file...")
                file_content = """#include <stdio.h>

int main() {
    printf("Hello, world!\\n");
    return 0;
}
"""
                file_extension = "c"
            elif generated == 6:
                print("Creating a commit with a Python file...")
                file_content = """print('Hello, world!') """
                file_extension = "py"
            elif generated == 7:
                print("Creating a commit with a Jupyter file...")
                file_content = """print('Hello, world!') """
                file_extension = "ipynb"
            elif generated == 8:
                print("Creating a commit with a JavaScript file...")
                file_content = """console.log('Hello, world!'); """
                file_extension = "js"
            elif generated == 9:
                print("Creating a commit with a TypeScript file...")
                file_content = """console.log('Hello, world!'); """
                file_extension = "ts"
            else:
                print("Creating a commit with a Brainfuck file...")
                file_content = """++++++++++[>+++++++>++++++++++>+++>+<<<<-]>++.>+.+++++++..+++.>++.<<+++++++++++++.>++++.--------.++++++++++++.--------.--------.
"""
                file_extension = "bf"

            print("Generating salt...")
            salt = generate_salt()
            file_path = os.path.join(proj_dir, f"Temp-{salt}.{file_extension}")
            with open(file_path, "w") as file:
                file.write(file_content)

            subprocess.run(["git", "init"], check=True)
            subprocess.run(["git", "add", file_path], check=True)
            subprocess.run(["git", "commit", "-m", f"Add Temp-{salt}.{file_extension}"], check=True)
            
            github_repo_url = f"https://github.com/{github_username}/{repository_name}.git"
            
            # Check if remote already exists, if not, add it
            remote_output = subprocess.run(["git", "remote", "get-url", "origin"], capture_output=True, text=True)
            if github_repo_url not in remote_output.stdout:
                subprocess.run(["git", "remote", "add", "origin", github_repo_url], check=True)
            
            # Clean untracked files
            subprocess.run(["git", "clean", "-f", "-d"], check=True)
            
            # Pull changes from the remote repository, allowing unrelated histories
            subprocess.run(["git", "pull", "origin", "master", "--allow-unrelated-histories"], check=True)
            
            # Push the changes to the remote repository
            subprocess.run(["git", "push", "-u", "origin", "master"], check=True)

            os.remove(file_path)
            commits += 1
            print(f"Commits: {commits}")
        except subprocess.CalledProcessError as e:
            print(f"Reloading due to {e}")

    time.sleep(10)
