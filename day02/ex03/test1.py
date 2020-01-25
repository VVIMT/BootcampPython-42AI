from csvreader import CsvReader

if __name__ == "__main__":
    with CsvReader('C:\\Users\\Vincent\\source\\repos\\Bootcamp-42AI\\day02\\ex03\\good.csv') as file:
        data = file.getdata()
        header = file.getheader()

        print(data)