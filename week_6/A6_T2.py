def writing(filename, firstName, lastName):
    with open(filename, 'w') as file:
        file.write(firstName+'\n')
        file.write(lastName)
              

def main():
    print("Program starting.")
    firstName = input("Insert first name: ")
    lastName = input("Insert last name: ")
    filename = input("Insert filename: ")
    writing(filename, firstName, lastName)
    print("Program ending.")
main()