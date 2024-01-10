# Contributing to Code Park

Thank you for considering contributing to Code Park! 🌳 Before you get started, please take a moment to review the guidelines below to ensure a smooth and collaborative experience.

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
- Do not modify or remove any folder or file in this reposity starting with (.) or all the letters are in uppercase. These are called admin files. Place an proper issue in github if you wanna suggest any modification here.
- Current we are only accepting codes in [c, c++], which is best for raw code and DSA.
   
5. **Before Submission:**
- Make sure you removed all the unnecessary folders/files.
- run **READY_REPO.cpp** which will update your changes into the DOCUMENTATION.md.

6. **Reasons for Direct Pull Request Rejection:**
- Modify any admin folder/file (starts with **.** or all uppercase).
- Absence/inappropriate comments in the code.
- Did not follow [code placement](#code-placement).
- Irrelevant commit message.

  
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

- Place your code or solution in a separate class or function. Avoid implementing it directly within the main function. Instead, utilize the main function for testing purposes.

- Refrain from using **typedef** or **define** macros to create shortcuts. Users may sometimes only copy the function without copying the macro definition, leading to potential bugs or build failures.

- Use large data types like **long long** or **double** instead of **int** or **float** to avoid unexpected bug for large argument.

## Submitting Contributions

Follow these steps to submit your contribution:

1. **Fork the Repository:** Click the "Fork" button on the Code Park repository.
2. **Create a Branch:** Create a new branch for your changes.
3. **Make Changes:** Add your code following the guidelines mentioned above.
4. **Commit Changes:** Commit your changes with descriptive commit messages.
5. **Push Branch:** Push your branch to your fork of the repository.
6. **Submit Pull Request:** Open a pull request with details about your changes.

if you see any messages like,
<p>Your branch and 'origin/master' have diverged</p>
do not panic, it means your repository is not sync with the original repository.
The simplest solution is,

- Copy your folder/file(your update) in a safe location and  [delete](https://docs.github.com/en/repositories/creating-and-managing-repositories/deleting-a-repository) the repository.
  
- Then follow the above [submitting contribution](#submitting-contributions) section again.

Thank you for contributing to Code Park! Your efforts help create a valuable resource for developers around the world.

Happy coding! 🚀
