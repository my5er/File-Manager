import os


class FileCreator:
    @staticmethod
    def start():
        file_directory = str(input('File Directory: '))
        file_name = str(input('File Name: '))
        file_type = str(input('File Type: '))
        try:
            file = os.path.join(file_directory, file_name + file_type)
            file1 = open(file, "w")
            file1.close()
            print(f'File {file_name + file_type} succesfuly created in {file_directory}')
        except FileExistsError:
            print(f'The file {file_name + file_type} already exists in {file_directory}!')
