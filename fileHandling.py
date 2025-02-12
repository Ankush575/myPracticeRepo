# python program to read file
# NOTE: Read (r) - Opens a file for reading. (default)
import csv


def readFile():
    try:
        with open('fileHandling.txt', 'r') as file:
            content = file.read()
            print('Content of the file:', content)

    except FileNotFoundError:
        print("File does not exist.")

    finally:
        print("Code executed successfully: ")


readFile()

# python program to write into a file
# NOTE: Write (w) - Opens the file for writing (Creates a new file or overwrites the existing one.)


def writeFile():
    try:
        with open('fileHandling.txt', 'w') as file:
            file.write(
                "This content has been added by myself to test the file handling.")

        with open('fileHandling.txt', 'r') as file:
            content = file.read()

            print("content:", content)
    except FileNotFoundError:
        print("Sorry file not found.")


writeFile()

# python program to append file
# NOTE: Append (a) - Opens the file for appending. (Creates a new file or appends to an existing one.)


def appendFile():
    try:
        with open('fileHandling.txt', 'a') as file:
            file.write("This is the appended line.\n")
        with open('fileHandling.txt', 'r') as file:
            content = file.read()
            print("Content of the file:", content)
    except Exception as e:
        print(f"Error {e} has occurred.")


appendFile()

# python program to operate on binary file.
# NOTE: Binary files are opened in binary mode and the file is read or written in bytes.
# read binary file


def readBinaryFile():
    try:
        with open('test.webp', 'rb') as file:
            content = file.read()
            print(content[:20])
    except FileNotFoundError:
        print("File not found.")
    except Exception as e:
        print(f"Error: {e}")


readBinaryFile()

# write binary file


def writeBinaryFile():
    try:
        with open('test.webp', 'wb') as file:
            file.write(b"I am writing into the binary file.")
    except FileNotFoundError:
        print("File not found.")
    except Exception as e:
        print(f"Error: {e}")


writeBinaryFile()


def appendBinaryFile():
    try:
        with open('test.webp', 'ab') as file:
            file.write(b"I am appending into the binary file.")
        with open('test.webp', 'rb') as file:
            content = file.read()
            print(content)
    except FileNotFoundError:
        print("File not found.")
    except Exception as e:
        print(f"Error: {e}")


appendBinaryFile()


# python program using exclusive mode
# NOTE: Exclusive (x) - Creates a new file. If the file already exists, the operation fails.
def exclusiveMode():
    try:
        with open('fileHandling.txt', 'x') as file:
            file.write("This is the exclusive mode.")
        with open('fileHandling.txt', 'r') as file:
            content = file.read()
            print(content, flush=True)
    except FileExistsError:
        print("File already exists.", flush=True)
    except Exception as e:
        print(f"Error: {e}")


exclusiveMode()

# python program to read file line by line


def readLineByLine():
    try:
        with open('fileHandling.txt', 'r') as file:
            for line in file:
                print(line, end='')
    except FileNotFoundError:
        print("File not found.")
    except Exception as e:
        print(f"Error: {e}")
    finally:
        print("Code executed successfully.")


readLineByLine()

# pythonprogram to read csv file using csv module


def readCsvFile():
    try:
        with open('testing.csv', 'r') as file:
            content = csv.reader(file)
            for row in content:
                print(row)

    except FileNotFoundError:
        print("File not found.")
    except Exception as e:
        print(f"Error: {e}")

    finally:
        print("Code executed successfully.")


readCsvFile()


# python program to write csv file using csv module


def writeCsvFile():
    try:
        data = [['Name', 'Age', 'city'],
                ['John Doe', 25, 'New York'],
                ['Jane Doe', 24, 'London'],
                ['John Smith', 26, 'Sydney']]
        with open('testing.csv', 'w') as file:
            writer = csv.writer(file)
            writer.writerows(data)
    except FileNotFoundError:
        print("File not found.")
    except Exception as e:
        print(f"Error: {e}")

    finally:
        print("Code executed successfully.")


writeCsvFile()

# python program to append csv file using csv module


def appendCsvFile():
    try:
        data = [['Name', 'Age', 'city'],
                ['John Doe', 25, 'New York'],
                ['Jane Doe', 24, 'London'],
                ['John Smith', 26, 'Sydney']]
        with open('testing.csv', 'a') as file:
            writer = csv.writer(file)
            writer.writerows(data)
    except FileNotFoundError:
        print("File not found.")
    except Exception as e:
        print(f"Error: {e}")

    finally:
        print("Code executed successfully.")


appendCsvFile()


# python program to  write, read and append data into the dictionary using csv file using csv module


def readAndWriteCsvFileUsingDictionary():
    try:
        data = [{'Name': 'John Doe', 'Age': 25, 'city': 'New York'},
                {'Name': 'Jane Doe', 'Age': 24, 'city': 'London'},
                {'Name': 'John Smith', 'Age': 26, 'city': 'Sydney'}]
        with open('dict.csv', 'w') as file:
            writer = csv.DictWriter(file, fieldnames=['Name', 'Age', 'city'])
            writer.writeheader()
            writer.writerows(data)

        with open('testing.csv', 'r') as file:
            reader = csv.DictReader(file)
            for row in reader:
                print(row)

        with open('testing.csv', 'a') as file:
            writer = csv.DictWriter(file, fieldnames=['Name', 'Age', 'city'])
            writer.writerow(
                {'Name': 'John Doe', 'Age': 25, 'city': 'New York'})
    except FileNotFoundError:
        print("File not found.")
    except Exception as e:
        print(f"Error: {e}")

    finally:
        print("Code executed successfully.")


readAndWriteCsvFileUsingDictionary()
