def main():
    print("Program starting.")
    word = ""
    while True:
        print("Options:\n1 - Insert word\n2 - Show current word\n3 - Show current word in reverse\n0 - Exit")
        choice =int(input("Your choice: "))
        if  choice == 1:
            word=input("Insert word: ")
        if choice == 2:
            print(f"Current word - \"{word}\"\n")
        if choice == 3:
            print(f"Current word in reverse - \"{word[::-1]}\"\n")
        if choice>3:
            print("Unknown option! try again.\n")
        if choice == 0:
                print("Exiting program.\n")
                break
    print("\nProgram ending.")

main()