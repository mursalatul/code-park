import os

class CreateDocumentation:
    def writedoc(self, folder_file: dict):
        with open("DOCUMENTATION.md", "w") as doc:
            doc.write("# Code Park Documentation\n\
This documentation provides a front view of the content presented in the repository. Here, you can see the folders and the files with a tree-view structure.\n\n")

            doc.write("## Content\n")
            for folder, file in folder_file.items():
                doc.write(f"- [{folder}](/{folder})\n")
                for files in file:
                    doc.write(f"  - [{files}](/{files})\n")

class Files:
    # this char will not accepted inside a class
    RESTRICTED_CHAR = [".", "-", "!", "@", "#", "$", "%", "^", "&", "*", 
                    "(", ")", "+", "=", "~", "`", "{", "}", "|", "\\",
                    ":", ";", "'", '"', ",", ".", "?", "/", " "]
    
    # special cases to restrict
    SPECIAL_FILES_TO_IGNORE = ["LICENSE", "venv"]
    
    # this languages only will be accespted to commit
    LENGUAGE_EXTENTION = [".cpp", ".c", ".py", ".java"]

    def __init__(self) -> None:
        pass

    def get_all_valid_folder_files_dict(self):
        # store all the data
        """
        structure:
        {
            folder1 : [file1, file2, .....],
            folder2 : [file1, file2, .....],
            .
            .
            .
        """
        all_files = {}
        cwd = os.getcwd()
        for folder_name in os.listdir(cwd):
            # works only for directory
            if os.path.isdir(os.path.join(cwd, folder_name)):
                # checking if folder_name contain any RESTRICTED_CHAR
                folder_status = self.goodfolderformat(folder_name)["status"]
                if folder_status == "ignore_folder" or folder_name in self.SPECIAL_FILES_TO_IGNORE:
                    pass
                elif folder_status == "1":
                    # store all the file names
                    file_names = []

                    # going inside the folder to get all the files
                    inside_folder_name = os.path.join(cwd, folder_name)

                    for file in os.listdir(inside_folder_name):
                        file_path = os.path.join(inside_folder_name, file)
                        if os.path.isfile(file_path):
                            # checking if the file is a valid file
                            file_status = self.good_file_format(file)["status"]
                            if file_status == '1' and file not in self.SPECIAL_FILES_TO_IGNORE:
                                file_names.append(file)
                            else:
                                # if wrong file found
                                return {"ERROR": file_status}

                    all_files[folder_name] = file_names
                else:
                    # if wrong formatted folder found
                    return {"ERROR" : folder_status}
        return (all_files)

    def isgoodname(self, name: str) -> dict:
        """
        check if the name contain any restricted character or not
        
        Parameters:
        - (str) name to check

        Returns
        - (dict) 
        "status" : 1 if not found any restricted character
        "status" : "restricted character" if restricted character found
        """
        for character_in_name in list(name): # converting str -> to iterater
            if character_in_name in self.RESTRICTED_CHAR:
                status =  {"status" : ""}
                # finding the restricted character and adding it in dict
                for c in self.RESTRICTED_CHAR:
                    if character_in_name == c:
                        status["status"] = c
                        return status
        return {"status": "1"}
    
    def good_file_format(self, file_name: str) -> dict:
        status = False
        for lang_ext in self.LENGUAGE_EXTENTION:
            if file_name.find(lang_ext) != -1:
                status = True
                break
        # if not from the LENGUAGE_EXTENTION
        if status == False:
            return {"status" : f"currectly only accepting codes on {self.LENGUAGE_EXTENTION}"}
        else:
            file_name_with_out_ext = []
            for c in list(file_name):
                if c != '.':
                    file_name_with_out_ext.append(c)
                else:
                    break
            return self.isgoodname("".join(file_name_with_out_ext))

    def goodfolderformat(self, folder_name: str) -> dict:
        if folder_name[:1] == ".":
            return {"status" : "ignore_folder"}
        else:
            return self.isgoodname(folder_name)


def main():
    ff = Files()
    data = (ff.get_all_valid_folder_files_dict())
    if "ERROR" in data:
        pass
    else:
        doc = CreateDocumentation()
        doc.writedoc(data)
if __name__ == '__main__':
    main()
