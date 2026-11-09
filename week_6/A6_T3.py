def reading(sourceFile, Content):
    print(f"Reading file '{sourceFile}' content.")
    with open(sourceFile, 'r') as file:
        row = file.read()
        Content += row
    print("File content ready in memory.")
    return Content
def writing(destinationFile, Content):
    print(f"Writing content into file '{destinationFile}'.")
    with open(destinationFile, 'w') as file:
        file.write(Content)
    print("Copying operation complete.")
    
def main():
    print("Program starting.")
    print("This program can copy a file.")
    sourceFile = input("Insert source filename: ")
    destinationFile = input("Insert destination filename: ")
    Content = ''
    Content = reading(sourceFile, Content)
    writing(destinationFile, Content)
    print("Program ending.")
    return None
main()