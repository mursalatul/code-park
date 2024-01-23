import os, json


class HandleJson:
    # reformat data as actual json format
    def add_link(self):
        self.dic = {
            # "folder_number" : f"{len(self.data)}",
            # "folder1" : {
            #     "folder1_url" : "",
            #     "file_number" : "",
            #     "file1" : "file1 url",
            #     "file2" : "file2 url"
            # },
        }

        for folder, file in self.data.items():
            inner_dic = dict()
            inner_dic["folder_url"] = "https://github.com/mursalatul/code-park/tree/master/" + folder
            #inner_dic["file_number"] = f"{len(file)}"
            # sort is working locally but is not working in github action. will fix it later
            # file.sort()
            for f in file:
                inner_dic[f] = inner_dic["folder_url"] + f"/{f}"
            self.dic[folder] = inner_dic
        

    def write_json(self, data):
        self.data = data
        self.add_link()
        with open("DOC_DATA.json", "w") as outfile: 
            json.dump(self.dic, outfile, indent=4)


class CreateDocumentation:
    def writedoc(self, folder_file: dict):
        
        with open("DOCUMENTATION.md", "w") as doc:
            doc.write("# Code Park Documentation\n\
This documentation provides a front view of the content presented in the repository. Here, you can see the folders and the files with a tree-view structure.\n\n")

            doc.write("## Content\n")

            # sorting the folders before adding to doc
            folder_file = dict(sorted(folder_file.items()))

            # getting folder name and file list
            for folder, file in folder_file.items():
                # writing folder name to doc
                doc.write(f"- [{folder}](https://github.com/mursalatul/code-park/tree/master/{folder})\n")
                # sorting the files for organized view in doc
                #file.sort()
                # adding the file names
                for files in file:
                    doc.write(f"  - [{files}](https://github.com/mursalatul/code-park/tree/master/{folder}/{files})\n")


class Files:
    # this char will not accepted inside a class
    RESTRICTED_CHAR = [".", "-", "!", "@", "#", "$", "%", "^", "&", "*", 
                    "(", ")", "+", "=", "~", "`", "{", "}", "|", "\\",
                    ":", ";", "'", '"', ",", ".", "?", "/", " "]
    
    # special cases to restrict
    # this folders will not be considered as regular folder to add in DOCUMENTATION.md
    SPECIAL_FILES_TO_IGNORE = ["LICENSE", "venv", "virtual_env", "env",
                            "environment", "ADMIN", "CONTENT"]
    
    # this languages only will be accespted to commit
    LENGUAGE_EXTENTION = [".cpp", ".c", ".py", ".java"]

    def get_all_valid_folder_files_dict(self, data_location):
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
        cwd = data_location

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
                                return {"ERROR": file_status,
                                        "target" : "file",
                                        "name" : file}

                    all_files[folder_name] = file_names
                else:
                    # if wrong formatted folder found
                    return {"ERROR" : folder_status,
                            "target" : "folder",
                            "name" : folder_name}
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
            if character_in_name in self.RESTRICTED_CHAR or (character_in_name >= 'A' and character_in_name <= "Z"):
                status =  {"status" : ""}
                # check if any upper case letter is used.
                if (character_in_name >= "A" and character_in_name <= "Z"):
                    status["status"] = f"upper case letter '{character_in_name}' used."
                else:
                    # finding the restricted character and adding it in dict
                    for c in self.RESTRICTED_CHAR:
                        if character_in_name == c:
                            status["status"] = c
                            break
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
    # getting repository location
    cwd = os.getcwd()

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
