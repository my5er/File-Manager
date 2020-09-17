import os
import shutil


class FileMover:
    @staticmethod
    def start():
        file_directory = str(input('File Directory: '))
        file_name = str(input('File Name: '))
        file_type = str(input('File Type: '))
        try:
            file = os.path.join(file_directory, file_name + file_type)
            os.mkdir(file)
            print(f"Couldn't find the file {file}.")
            os.remove(file)

        except FileExistsError:
            for root, directories, files in os.walk(file_directory):
                for file in files:
                    if file_name in file:
                        moved_file = os.path.join(file_directory, file_name + file_type)
                        new_directory = str(input('New Directory: '))
                        new_file_directory = os.path.join(new_directory, file_name + file_type)
                        shutil.move(moved_file, new_file_directory)
                        print(f'File {moved_file} moved to {new_directory}')



