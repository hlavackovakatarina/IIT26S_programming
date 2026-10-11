list = []
step=0
print("Program starting.")
integer = int(input("Insert positive integer: "))
list.append(integer)
while integer > 1:
    step += 1
    division = integer % 2
    if division == 0:
        integer = integer // 2
        list.append(integer)
    elif division != 0:
        integer= 3*integer + 1
        list.append(integer)
print(str(list).strip("[]").replace(",", " -> "))
print(f"Sequence had {step} total steps.")
print("\nProgram ending.")