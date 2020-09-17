import os


class FileEreaser:
    @staticmethod
    def start():
        file_directory = str(input('File Directory: '))
        file_name = str(input('File Name: '))
        file_type = str(input('File Type: '))

        try:
            file = os.path.join(file_directory, file_name + file_type)
            os.mkdir(file)
            print(f"Couldn't find the file {file}")

        except FileExistsError:
            for root, directory, files in os.walk(file_directory):
                for file in files:
                    if file_name in file:
                        deleted_file = os.path.join(root, file)
                        os.remove(deleted_file)
                        print(f'File {deleted_file} deleted.')
