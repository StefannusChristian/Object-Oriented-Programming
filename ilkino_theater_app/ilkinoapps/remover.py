import os


class TxtRemover:
    def files_in_path(self):
        path = '\Kuliah\oop_ilkino'
        files = os.listdir(path)
        return files

    def find_txt_files(self):
        files = self.files_in_path()
        txt_files = []
        for f in files:
            if f[-3:] == 'txt':
                txt_files.append(f)
        return txt_files

    def remove_files(self):
        txt_files = self.find_txt_files()
        for files in txt_files:
            if os.path.exists(files):
                os.remove(files)

    def delete_txt_files(self):
        self.remove_files()
