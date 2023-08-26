# GitHub Commits Farm
A program that will farm and create commits on your GitHub account.

## Introduction
This project was created simply to farm GitHub commits on your account for 3 reasons:
<br>
1. Keep your account active.
2. Look cool.
3. Flex on your friends the fact that your life is just non-existent.

## Results
A long time ago I have create a very simple version and tested it on an alternative account and these were the results:
<br>
<br>
![112,000 commits on GitHub](src/results.jpg)

## How it works?
You might wonder what is the formula used by this program
<br>
This program does a simple operation using the built-in Python module `random` to generate a random integer from 1 to 10.
After choosing a number, if the number is 1, 2 or 3 it waits 15 seconds then chooses another number.
The rest of the numbers correspond to a progrmamming language that the program writes a simple script with to output "Hello, world!" then publish the file on GitHub with the name Temp- then a random salt then the file type of that programming language.
<br>
Here are the programming languages the numbers correspond to:
<br>
<br>
4. C++
<br>
5. C
<br>
6. Python
<br>
7. Jupyter
<br>
8. JavaScript
<br>
9. TypeScript
<br>
10. Brainfuck
<br>

## How to use
Using this program is very simple.
If you look in the files of this repository you will find a file called `main.py` containing the code.
All you have to do is create an empty folder, create a python file inside of it and insert the code, change the username with yours and write the name of an empty repository on your account to be used then run the program using any Python interpreter.

1. Install [Git Bash](https://git-scm.com/downloads) and run the installer.
2. After setting Git Bash, enter the command `git config --global user.name "Your Name"` and replace Your Name with your actual name.
3. After running that first command run the other command `git config --global user.email "user@domain.com"` and replace user@domain.com with the email you used to sign up for GitHub.
4. Copy the contents of the file `main.py` from this repository.
5. Create an empty repository on your account (preferably with the name `commit`).
6. Create an empty folder on your computer dedicated to this program.
7. Create a Python file in that new folder and paste the program's code inside of it.
8. Change the username inside (currently written mine) and change the GitHub repository to the name of the GitHub repository you created.
9. Run the program using any Python interpreter.

*The program should now work. If any errors or issues occur, don't hesitate to create an issue here in this repository.*
<br>
<br>

**WARNING: DO NOT RUN THIS SCRIPT IN THE DESKTOP OR ANY DIRECTORY SIMILAR TO THAT. PLEASE CREATE A FOLDER DEDICATED TO THIS FARM TO PREVENT ISSUES WITH YOUR COMPUTER OR RANDOM FILES APPEARING ON YOUR COMPUTER.**

## License
This project is under the `MIT License`. Please check `LICENSE` for more information.

## **Thank you for viewing this repository and happy farming**
