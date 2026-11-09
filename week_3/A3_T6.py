print("Program starting.")
print("Welcome to the unit converter program!")
print("Follow the menu instructions below.\n")
option = int(input("Options:\n1 - Lenght\n2 - Weight\n0 - Exit\nYour choice: "))
if option == 1:
    print("\nLenght options:")
    choice = int(input("1 - Meters to kilometers\n2 - Kilometers to meters\n0 - Exit\nYour choice: "))
    if choice == 1:
        meter = float(input("Insert meters: "))
        print(f"{round((meter),1)} m is {round((meter / 1000),1)} km")
    if choice == 2:
        km = float(input("Insert kilometers: "))
        print(f"{round((km),1)} km is {round((km * 1000),1)} m")
    if choice > 2:
        print("Unknown option.")
    if choice == 0:
        print("Exiting...")
if option == 2:
    print("Weight options:")
    choose =int(input("\n1 - Grams to pounds\n2 - Pounds to grams\n0 - Exit\nYour choice: "))
    if choose == 1:
        gram=float(input("Insert grams: "))
        print(f"{gram} g is {round(gram * 0.002205, 1)} lb")
    if choose == 2:
         lb=float(input("Insert pounds: "))
         print(f"{lb} lb is {round(lb * 453.6, 1)} g")
    if choose == 0:
        print("Exiting...")
    if choose > 2:
        print("Unknown option.")
if option == 0:
    print("\nExiting...")
if option > 2:
    print("Unknown option")
print("\nProgram ending.")

