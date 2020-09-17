import os
import shutil


class FileCopier:
    @staticmethod
    def start():
        file_directory = str(input('File Directory: '))
        file_name = str(input('File Name: '))
        file_type = str(input('File Type: '))
        try:
            file = os.path.join(file_directory, file_name + file_type)
            os.mkdir(file)
            print(f"Couldn't find the file {file}.")
            os.rmdir(file)
        except FileExistsError:
            for root, directories, files in os.walk(file_directory):
                for file in files:
                    if file_name in file:
                        copied_file = os.path.join(file_directory, file_name + file_type)
                        copied_file_directory = str(input('Directory to paste copied file: '))
                        paste_file_directory = os.path.join(copied_file_directory, file_name + file_type)
                        shutil.copy(copied_file, paste_file_directory)
                        print(f'File {copied_file} copied to {copied_file}')
