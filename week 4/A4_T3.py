
list = []
print("Program starting.\n")
start=int(input("Insert starting value: "))
end=int(input("Insert stopping value: "))
print("\nStarting for-loop:")
while start <= end:
    list.append(start)
    start += 1
print(str(list).strip("[]").replace(",", ""), end="")
print("\nProgram ending.")