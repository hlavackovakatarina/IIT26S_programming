print("Program starting.")
print("This is a program with simple menu, where you can choose which operation the program performs.")
name=input("Before the menu, please insert your name: ")
option=int(input("\nOptions:\n1 - Print welcome message\n2 - Print the name backwards\n3 - Print the first character\n4 - Show the amount of characters in the name\n0 - Exit\nYour choice: "))
if option == 1:
    print(f"Welcome {name}!")
elif option == 2:
    print(f"Your name backwards is \"{name[::-1]}\"")
elif option == 3:
    print(f"The first character in name \"{name}\" is \"{name[0]}\"")
elif option == 4:
    print(f"There are {len(name)} characters in the name \"{name}\"")
elif option == 0:
    print("Exiting...")
else:
    print("Unknow option.")
print("\nProgram ending.")

