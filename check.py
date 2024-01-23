import os

from UPDATE_DOC import Files


def main():
    # welcome message
    print("Preparing the repository for commit.".center(50, "*"))
    print("\nFolder/File naming format checking . . . . . . . .")
    ff = Files()
    data = (ff.get_all_valid_folder_files_dict(os.getcwd()))
    if "ERROR" in data:
        # show relevent error message
        # if error with the folder name
        if data["target"] == "folder":
            # show error message and relavent error(RESTRICTED_CHAR)
            print(f"Wrong folder naming. \nYou have used \"", data["ERROR"], "\" in your folder name", sep="")
            # show the folder name with error
            print("->", data["name"])
        # if error with file name
        else:
            # show error message and relavent error(RESTRICTED_CHAR)
            print(f"Wrong file naming. \nYou have used \"", data["ERROR"], "\" in your folder name", sep="")
            # show the file name with error
            print("->", data["name"])
        print("\nChecking process ended with error!")
    else:
        print("Checking process ended. All Folder/File names are seems good!\nYou are ready to commit and push/pull request")
        
        # ending message
        print("\nSome key points to remember:")
        print("* make sure you are running this program just before the commit.\n\
* DOCUMENTATION.md will be auto updated after your pull request accepted.\n\
* do not modify this program. this is build to reduce your effort.\n\
* if you find any bug/suggestion feel free to submit an issue at\n\
https://github.com/mursalatul/code-park/issues/new \n\
* see the CONTRUBUTION.md(https://github.com/mursalatul/code-park/blob/master/CONTENT/CONTRIBUTE.md)\n\
if you are confused about contributing in this project.\n")

if __name__ == '__main__':
    main()

