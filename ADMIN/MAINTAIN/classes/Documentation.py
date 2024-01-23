import os

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
                doc.write(f"- [{folder}](/{folder})\n")
                # sorting the files for organized view in doc
                file.sort()
                # adding the file names
                for files in file:
                    doc.write(f"  - [{files}](/{files})\n")