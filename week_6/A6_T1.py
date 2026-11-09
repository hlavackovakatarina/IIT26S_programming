def reading(filename):
    file = open(filename, 'r')
    text = file.read()
    while text != '':
        print(text)
        text = file.read()
    file.close()
def main():
    print("Program starting.")
    print("This program can read a file.")
    filename = input("Insert filename: ")
    print(f"### START {filename} ###")
    text = reading(filename)
    print(f"### END {filename} ###")
    print("Program ending.")
    return None
main()