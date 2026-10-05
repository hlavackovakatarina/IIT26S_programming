
print ("Program starting.\n")
start=int(input("Enter starting value: "))
end=int(input("Enter stopping value: "))
print("\nStarting for-loop:") 
for i in range(start, end+1):
    list = [i for i in range(start, end+1)]
print(str(list).strip("[]").replace(",", ""), end="")
print("\nProgram ending.")