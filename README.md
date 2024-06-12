# GitHub Commits Farm
A program that will farm and create commits on your GitHub account.

This project was created simply to farm GitHub commits on your account for a cooler profile and keeping your account active:

## Results
A long time ago I have create a very simple version and tested it on an alternative account and these were the results:
<br>
<br>
![112,000 commits on GitHub](src/results.jpg)

## How it works
You might wonder what is the formula used by this program
<br>
This program does a simple operation using the built-in Python module `random` to generate a random integer from 1 to 10.
After choosing a number, if the number is 1 or 2 it waits 15 seconds then chooses another number.
The rest of the numbers correspond to a progrmamming language that the program writes a simple script with to output "Hello, world!" then publish the file on GitHub with the name Temp- then a random salt then the file type of that programming language.
<br>
Here are the programming languages the numbers correspond to:
<br>
<br>
3. Dart
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
1. Install [Git Bash](https://git-scm.com/downloads) and run the installer.
2. Create an empty folder on your computer dedicated to this program.
3. In your new folder, clone this repository using the command `git clone https://github.com/SelimWaly/commits-farm.git`.
4. After cloning, enter into the repository's folder using the command `cd commits-farm`.
5. Use a Python interpreter of your choice to run the file `main.py`.

Here are the commands to copy and paste into your terminal to execute all at once:
```sh
git clone https://github.com/SelimWaly/commits-farm.git
cd commits-farm
python main.py
```

*The program should now work. If any errors or issues occur, don't hesitate to create an issue here in this repository.*
<br>
<br>

> [!WARNING]\
> Do not run this script on your desktop or any directory with similar importance. Please create a folder dedicated to this farm to prevent issues with your computer such as random files appearing on your computer.

## License
This project is under the `MIT License`. Please check `LICENSE` for more information.

## **Thank you for viewing this repository and happy farming!**
