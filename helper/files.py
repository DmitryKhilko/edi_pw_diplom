import os


class FilesWork:
    @staticmethod
    def write_file(file_name, writable_string):
        with open('./' + file_name, "a+", encoding="utf8") as file:
            file.write(writable_string + '\n')

    @staticmethod
    def read_file(file_name):
        if os.path.isfile(f'./{file_name}'):
            with open('./' + file_name, "r", encoding="utf8") as file:
                for line in file:
                    return line

    @staticmethod
    def delete_file(file_name):
        if os.path.isfile(f'./{file_name}'):
            os.remove(f'./{file_name}')
