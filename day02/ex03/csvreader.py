class CsvReader():
    def __init__(self, filename, sep=',', header=False, skip_top=0, skip_bottom=0):
        self.file = None
        self.filename = filename

        print("init method of MyContext")

    def __enter__(self):
        print("entering context of MyContext")
        self.file = open(self.filename)
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        print("exit context of MyContext")

    def getdata(self):
        return self.__enter__()

#getheader()
