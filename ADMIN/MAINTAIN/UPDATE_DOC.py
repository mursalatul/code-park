import os
from classes.Files import Files
from classes.Documentation import CreateDocumentation
from classes.handle_json import HandleJson



def main():
    # getting file data
    ff = Files()
    data = (ff.get_all_valid_folder_files_dict())
    
    # writing to Documentation.md
    doc = CreateDocumentation()
    doc.writedoc(data)

if __name__ == '__main__':
    main()
