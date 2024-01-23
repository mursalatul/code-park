import json, os

class HandleJson:
    # reformat data as actual json format
    def add_link(self):
        self.dic = {
            "folder_number" : f"{len(self.data)}",
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
            inner_dic["file_number"] = f"{len(file)}"
            # sort is working locally but is not working in github action. will fix it later
            # file.sort()
            for f in file:
                inner_dic[f] = inner_dic["folder_url"] + f"/{f}"
            self.dic[folder] = inner_dic
        

    def write_json(self, data):
        self.data = data
        self.add_link()
        with open("DOC_DATA.json", "w") as outfile: 
            json.dump(self.dic, outfile)