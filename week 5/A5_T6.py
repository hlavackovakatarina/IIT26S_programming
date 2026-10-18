def main():
    print("Program starting.")
    count = 0
    while True:
        print("Options:\n1 - Show count\n2 - Increase count\n3 - Reset count\n0 - Exit")
        choice =input("Your choice: ")
        if choice == "1":
            print(f"Current count - {count}\n")
        elif choice == "2":
            count+=1
            print(f"Count increased!\n")
        elif choice == "3":
            count=0
            print(f"Cleared count\n")
        elif choice == "0":
            print("Exiting program.\n")
            break
        else:  
                print("Unknown option!\n")
    print("Program ending.")
    return None
main()