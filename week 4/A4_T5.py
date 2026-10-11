print("Program starting\n")
list1=[]
list2=[]
start=int(input("Insert starting point: "))
end=int(input("Insert stopping point: "))
inspection =int(input("Insert inspection point: "))
print()
if start >= end:
    print("Starting point value must be less than the stopping point value.")
if inspection < start or inspection > end:
    print("Inspection value must be within the range of start and stop.")
if start < end and inspection >= start and inspection <= end:
    print("\n First loop - inspection with break")
    for i in range(start, end):
        if i == inspection:
            break
        list1.append(i)
    print(str(list1).strip("[]").replace(",", ""), end="")
    print("\n Second loop - inspection with continue")
    for i in range(start, end):
        list2.append(i)
        if i == inspection:
            continue
    print(str(list2).strip("[]").replace(",", ""), end="")
print("\nProgram ending.")
