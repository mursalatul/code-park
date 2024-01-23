# Contributing to Code Park

Become part of our Code Park family by contributing. Your support not only adds you to our community but also fuels the spread of knowledge! 🌳 Before you get started, please take a moment to review the guidelines below to ensure a smooth and collaborative experience.

## Table of Contents
- [General Guidelines](#general-guidelines)
- [Structure](#structure)
- [Code Placement](#code-placement)
- [Coding Style](#coding-style)
- [Submitting Contributions](#submitting-contributions)

## General Guidelines

1. **Be Respectful:** Always be courteous and respectful towards other contributors. Encourage a positive and inclusive community.

2. **Avoid Binary and Executable Files:** Please refrain from uploading any binary or executable files. The focus of this repository is on clear and concise code implementations.

3. **Follow Code Etiquette:** Ensure that your code is well-commented for clarity. Follow the coding standards relevant to the language you are using.

4. **Restrictions:**
- Do not modify or remove any folder or file in this reposity starting with (.) or all the letters are in uppercase. These are called admin files. Place an proper [issue](https://github.com/mursalatul/code-park/issues/) in github if you wanna suggest any modification here.
- Currently we are only accepting codes in [c, c++, py, java], which is best for raw code and DSA.
   
5. **Before Submission:**
- Make sure you removed all the unnecessary folders/files.
- run **READY_REPO.py** which will check the status of your updates.

6. **Reasons for Direct Pull Request Rejection:**
- Modify any admin folder/file (starts with **.** or all uppercase).
- Absence/inappropriate comments in the code.
- Did not follow [code placement](#code-placement).
- Irrelevant commit message.

7. **Python dev**
- If you are using any virtual environment, make sure its name is one of ["venv", "virtual_env", "environment"]
  
## Structure

The repository is organized into folders based on different topics and programming languages. To maintain a structured and organized codebase, please adhere to the following guidelines:

#### Folder Naming:
- Use meaningful and descriptive names for folders.
- Avoid using spaces or special characters in folder names and always use lowercase letters.
- Example: "this_is_a_folder"

#### Code File Naming:
- Use filenames that clearly represent the content of the code.
- Avoid using spaces or special characters in file names and always use lowercase letters.
- Avoid generic names like `temp.txt` or `test.c`.
- Example: "this_is_a_file.cpp"

## Code Placement

If you want to contribute code on a specific topic and there is already an existing folder related to that topic, please follow these guidelines:

1. **Existing Folder:** If a relevant folder already exists, do not create a new one.
2. **File Placement:** Place your code file directly inside the existing folder.
3. **Folder Creation:** Only create a new folder if there is no existing folder related to your code topic.

**DO NOT CREATE NESTED FOLDER**

## Coding Style
We believe that a coder is an artist, and we cannot teach an artist how to be creative. Therefore, feel free to write code as you wish. However, to reduce bugs and improve performance, please follow the rules below:

- Place your code or solution in a separated class or function. Avoid implementing it directly within the main function. Instead, utilize the main function for testing purposes.

- Refrain from using **typedef** or **define** macros to create shortcuts. Users may sometimes only copy the function without copying the macro definition, leading to potential bugs or build failures.

- Use large data types like **long long** or **double** instead of **int** or **float** to avoid unexpected bug for large argument.

- Use [snake_case](https://en.wikipedia.org/wiki/Snake_case) naming convention.

Example Code:
```
#include<stdio.h>

/*
return summation of two number.

@param number1
@param number2

@return sum of number1 and number2
*/
long long sum(long long a, long long b)
{
   // returning sum of the numbers
   return a + b;
}

int main()
{
   int x = 1, y = 2;
   int sum = sum()
}
```

## Submitting Contributions

Follow these steps to submit your contribution:

1. **[Fork the Repository](https://docs.github.com/en/pull-requests/collaborating-with-pull-requests/working-with-forks/fork-a-repo#forking-a-repository):** Click the "Fork" button on the Code Park repository.
2. **Create a Branch:** Create a new branch for your changes.
3. **Make Changes:** Add your code following the guidelines mentioned above.
4. **Commit Changes:** Commit your changes with descriptive commit messages.
5. **Push Branch:** Push your branch to your fork of the repository.
6. **Submit Pull Request:** Open a pull request with details about your changes.

if you are working locally(obviously after [cloning](https://docs.github.com/en/pull-requests/collaborating-with-pull-requests/working-with-forks/fork-a-repo#cloning-your-forked-repository) your forked repository),

it is always recommanded to use **git pull** command before making any change in the repository. If you get **Already up to date.** then your repository already synced with the original repository. Else it will be synced.

If you are using vs code, make sure you installed [GitLens](https://marketplace.visualstudio.com/items?itemName=eamodio.gitlens) for better support.

![image](https://github.com/mursalatul/code-park/assets/79168756/0422214a-f2e9-4959-a12b-0bfb8acde8cb)

and before start doing your work, press the button at the left buttom,

![image](https://github.com/mursalatul/code-park/assets/79168756/ed4533f9-68a1-4164-bb4e-78420a77bb59)

If you are using tarminal/cmd/powershell, use **git push**,
If you see any messages like,
<p>Your branch and 'origin/master' have diverged</p>
it means your repository is not synced with the original repository but you made a change.
Do not panic,The simplest solution is,

- Copy your folder/file(your update) in a safe location and  [delete](https://docs.github.com/en/repositories/creating-and-managing-repositories/deleting-a-repository) the repository.
  
- Then follow the above [submitting contribution](#submitting-contributions) section again.

If you encounter difficulties contributing via GitHub, Please search the internet and read some documentations. There is no alternative method for contribution outside of GitHub

<h3>Thank you for contributing to Code Park! Your efforts help create a valuable resource for developers around the world.</h3>

**Happy coding! 🚀**
