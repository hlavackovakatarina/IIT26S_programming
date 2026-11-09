# use this one only with A6_T1_D1.txt
def readFile(filename: str) -> str: #str just telling it's like information
    FileHandler = open(filename, 'r', encoding = "UTF-8")
    Content = ''
    row = FileHandler.readline()
    while row != '':
        Content += row
        row = FileHandler.readline()
    FileHandler.close()
    return Content
def main():
    print("Program starting.")
    print("This program can read a file.")
    filename = input("Insert filename: ")
    FileContent = readFile(filename)
    print(f"### START {filename} ###")
    print(FileContent)
    print(f"### END {filename} ###")
    print("Program ending.")
    return None
main()