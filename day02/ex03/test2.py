from csvreader import CsvReader

if __name__ == "__main__":
    with CsvReader('C:\\Users\\Vincent\\source\\repos\\Bootcamp-42AI\\day02\\ex03\\bad.csv') as file:
        if file == None:
            print("File is corrupted")