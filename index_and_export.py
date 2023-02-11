class ExportSettings:
    def __init__(self):
        self.extension = None
        self.search_dir = ""
        self.export_dir = ""
        self.index_recursively = True

class Extension:
    def __init__(self, dir):
        self.dir = dir

    def assignParamsFromDir(self):
        #Open self.dir
        pass

def export():
    print("test print")