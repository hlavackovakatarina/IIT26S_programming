print("Program starting.")
print("Testing decision structures.")
integer=int(input("Insert an integer: "))
option=int(input("Options:\n1 - In one milti-branched decision\n2 - In multiple independent if statements\n0 - exit\nYour choice: "))
if option == 1:
    print("Using one multi-branched decision structure.")
    if integer >= 400:
        result = integer + 44
    elif integer >= 200:
        result = integer + 22
    elif integer >= 100:
        result = integer + 11
    print(f"Result is {result}")
if option == 2:
    print("Using multiple independent if-statements structure.")
    if integer >= 400:
        integer = integer + 44
    if integer >= 200:
        integer = integer + 22
    if integer >= 100:
        integer = integer + 11
    print(f"Result is {integer}")
if option == 0:
    print("Exiting...")
if option > 2:
    print("Unknown option.") 
print("\nProgram ending.")    