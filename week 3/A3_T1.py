print('Program starting.')
print("Insert two integers.")
one=int(input("Insert first integer: "))
two=int(input("Insert second integer: "))
print("Comparing inserted integers.")
if one>two:
    print("First integer is greater.\n")
elif two>one:
    print("Second integer is greater.\n")
else:
    print("Integers are the same\n")
print("Adding integers together")
print(f"{one} + {two} = {one+two}\n")
print("Checking the party of the sum...")
if (one+two)%2==0:
    print(f"The sum is even.")
else:
    print(f"The sum is odd.")
print("Program ending.")
