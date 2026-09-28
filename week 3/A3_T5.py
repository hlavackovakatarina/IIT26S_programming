print("Program starting.\n")
option=int(input("\nOptions:\n1 - Celsius to Fahrenheit\n2 - Fahrenheit to Celsius\n0 - Exit\nYour choice: "))
if option == 1:
    degrees=float(input("Insert the amount of Celsius: "))
    print(f"{degrees} °C equals to {round(((degrees*1.8)+32),1)} °F")
if option == 2:
    degrees=float(input("Insert the amount of Fahrenheit: "))
    print(f"{degrees} °F equals to {round(((degrees - 32)/1.8),1)} °C")
if option == 0:
    print("Exiting...")
if option > 2:
    print("Unknown option.")
print("\nProgram ending.")
