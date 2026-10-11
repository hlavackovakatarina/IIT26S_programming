print("Program starting.\n")
print("Check multiplicative persistence.")
integer = input("Insert an integer: ")
step = 0
while len(integer) > 1:
    step +=1
    result = 1
    calculation = ""
    for i in range(len(integer)):
        result *= int(integer[i])
        if calculation == "":
            calculation += integer[i]
        else:
            calculation = calculation + " * " + integer[i]  
    print(calculation, "=", result)
    integer = str(result)
print("No more steps.\n")
print(f"This program took {step} step(s)\n")
print("Program ending.")

            