#include <iostream>
#include <algorithm>
#include <filesystem>
#include <vector>
#include <fstream>

namespace fs = std::filesystem;

// functions pre-declaration

bool is_source_code_file(std::string file_name);
bool good_name(std::string name);
bool update_documentation(std::vector<std::string> folders, std::vector<std::pair<std::string, std::string>> files);

// main function
int main()
{
    try
    {
        // intro
        std::cout << "read_repository is a special program specifically written for this repository to auto generate DOCUMENTATION.md\n\
        * Make sure you are running this program just before commit a change.\n\
        * Do not change/modify this program.\n\
        * Please read the CONTRIBUTE.md to insure you are following all \n\
        the rules for contribute in this project\n\
        (https://github.com/mursalatul/code-park/blob/master/CONTRIBUTE.md).\n\
        * You will see a positive message if all goes well.\n\
        \nProcess started\n";
        // all folder list
        std::vector<std::string> folders;
        // all source code file list
        std::vector<std::pair<std::string, std::string>> files; // here first = file name, second = directory name

        // taking the currect path of all the folders
        std::string path = fs::current_path().string();

        // iterate all the folder and source codes and store them in the above vectors
        for (const auto &entry : fs::directory_iterator(path))
        {
            // folder
            if (fs::is_directory(entry.status()))
            {
                // check for valid folder name store it
                if (good_name(entry.path().filename()))
                {
                    folders.push_back(entry.path().filename());

                    // go to the valid folder and store files in the folder
                    std::string path_in_folder = entry.path().string();
                    for (const auto &entry2 : fs::directory_iterator(path_in_folder))
                    {
                        if (fs::is_regular_file(entry2.status()))
                        {
                            // check for valid file name and store it
                            if (is_source_code_file(entry2.path().filename()))
                            {
                                files.push_back({entry2.path().filename(), entry.path().filename()});
                            }
                        }
                    }
                }
            }
        }

        // sorting folder and file name for better view in the documentation.
        std::sort(folders.begin(), folders.end());
        std::sort(files.begin(), files.end());

        // updating documentation
        bool status = update_documentation(folders, files);
        if (status)
        {
            std::cout << "Process completed!\nDOCUMENATION.md has been successfully updated.\n";
            std::cout << "\nCheck DOCUMENTATION.md for changes.\nHappy Coding!\n";
        }
        else
            std::cout << "Process Failed!\nDOCUMENATION.md update failed.\n";
    }
    catch (const fs::filesystem_error &ex)
    {
        std::cerr << "Error accessing directory: " << ex.what() << std::endl;
    }
    return 0;
}

// function definition

/*
check if the file is a valid source code file

Parameters:
file name (string)

Return:
bool: true if file is a correct source code file, else false
*/
bool is_source_code_file(std::string file_name)
{
    // check if the file is a valid file
    std::string language_extension[] = {".c", ".cpp", ".py", ".java"};
    for (std::string extension : language_extension)
    {
        size_t extension_index = file_name.find(extension);
        if (extension_index != std::string::npos)
        {
            //
            std::string name_with_out_extension = file_name.substr(0, extension_index);
            // check if the name is good name or not
            if (good_name(name_with_out_extension))
                return true;
        }
    }
    return false;
}

/*
check if a name using proper format or not.
Example, a name (file/folder) can not contain any special char

Parameter:
string: file or folder name to check

Return:
bool: true if the name format is good, else false.
*/
bool good_name(std::string name)
{
    // check if the name contain any special character
    std::string exclude_char_list[] = {".", "-", "!", "@", "#", "$", "%", "^", "&", "*", "(", ")", "+", "=", "~", "`", "{", "}", "|", "\\", ":", ";", "'", "\"", ",", ".", "?", "/"};
    for (std::string exclude_char : exclude_char_list)
    {
        // if special char found return false
        size_t index = name.find(exclude_char);
        if (index != std::string::npos)
            return false;
    }

    // check if the  name contail any upper case letter
    for (char name_letter : name)
    {
        // return false if upper case found
        if (name_letter >= 'A' && name_letter <= 'Z')
            return false;
    }

    // name is good
    return true;
}

/*
update the DOCUMENTATION.md with updated new folders and files

Parameters:
vector 1: folder
vector 2: file

Return:
bool: true if the update process complete, else false
*/
bool update_documentation(std::vector<std::string> folders, std::vector<std::pair<std::string, std::string>> files)
{
    std::string filename = "DOCUMENTATION.md";
    // Open the file in reading and writing mode
    std::fstream fileStream(filename, std::ios::out);

    // store status
    bool status = false;

    // Write lines to the file
    if (fileStream.is_open())
    {
        // adding heading
        fileStream << "# Code Park Documentation\nThis document encompasses all the current subjects within Code Park.\
        \n\n## Folders\n";

        // adding folders
        for (std::string folder_name : folders)
            fileStream << "- [" << folder_name << "](/" << folder_name << ")\n";

        // adding files
        fileStream << "\n## Files\n";
        for (std::pair<std::string, std::string> f : files)
            fileStream << "- [" << f.first << "](/" << f.second << "/" << f.first << ")\n"; // file.first -> file name, file.second -> folder name

        // Close the file
        fileStream.close();

        status = true;
    }
    else
    {
        std::cerr << "Error opening file " << filename << " for writing." << std::endl;
        status = false;
    }
    return status;
}
