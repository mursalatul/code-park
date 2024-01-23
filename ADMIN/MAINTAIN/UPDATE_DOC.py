import os
from classes.Files import Files
from classes.Documentation import CreateDocumentation
from classes.handle_json import HandleJson



def main():
    # getting repository location
    cwd = os.getcwd()
    cwd = os.path.abspath(os.path.join(cwd, "..", "..")) # change cwd to repo home

    # getting file data
    ff = Files()
    data = (ff.get_all_valid_folder_files_dict(cwd))
    print(data)

    # writing to Documentation.md
    doc = CreateDocumentation()
    doc.writedoc(data) # documentation will be written in the repo home

    # updating the json file
    mjson = HandleJson()
    mjson.write_json(data)
    
if __name__ == '__main__':
    main()
