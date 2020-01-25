class CsvReader():
    def __init__(self, filename, sep=',', header=False, skip_top=0, skip_bottom=0):
        self.filename = filename
        self.sep = sep
        self.header = header
        self.skip_top = skip_top
        self.skip_bottom = skip_bottom

    def __enter__(self):
        try:
            with open(self.filename, "r") as f:
                raw_data = list(f)
        except FileNotFoundError:
            print(f"No such file {self.filename}")
            self.csv = None
            return self
        data = [line.replace("\"", "").replace("\n", "").replace("\t", "").replace(" ", "") for line in raw_data]
        self.header = data[0].split(",") if self.header else None
        if self.skip_top:
            data = data[1:]
        if self.skip_bottom:
            data = data[:-1]
        self.csv = [line.split(self.sep) for line in data]
        lines_length = []
        for line in self.csv:
            if '' in line:
                line.remove('')
            lines_length.append(len(line))
        if max(lines_length) != min(lines_length):
            return None

        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        if exc_type == FileNotFoundError:
            print(f"No file found {exc_val}")
            return -1
        if exc_type == AttributeError:
            print(f"bad format csv")
            return None

    def getdata(self):
        if self is None:
            return None
        return self.csv

    def getheader(self):
        if self is None:
            return None
        return self.header
