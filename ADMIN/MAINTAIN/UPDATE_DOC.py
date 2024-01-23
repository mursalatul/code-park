import os
from classes.Files import Files
from classes.Documentation import CreateDocumentation
from classes.handle_json import HandleJson



def main():
    # getting repository location
    cwd = os.getcwd()
    cwd = os.path.abspath(os.path.join(cwd, "..", ".."))

    # getting file data
    ff = Files()
    data = (ff.get_all_valid_folder_files_dict(cwd))
    print(data)

    # writing to Documentation.md
    doc = CreateDocumentation()
    doc.writedoc(data, cwd)

if __name__ == '__main__':
    main()
