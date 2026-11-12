def main():
    print("Program starting.")
    filename = input("Insert filename: ")
    analyseNumbers(filename)
    print("Program ending.")

def analyseNumbers(filename):
    print("#### Number analysis - START ####")
    with open(filename, 'r') as file:
        for line in file:
            line = line.strip()
    count = countNumbers(filename)
    sumNumber = sumNumbers(filename)
    greatest = greatestNumber(filename)
    average_Number = averageNumber(filename)
    print("Count;Sum;Greatest;Average")
    print(f"{count};{sumNumber};{greatest};{average_Number}")
    print("\n#### Number analysis - END ####")

def countNumbers(filename):
    count = 0
    with open(filename, 'r') as file:
        for line in file:
            line = line.strip()
            count += 1
    return count   

def sumNumbers(filename):
    sumNumber = 0
    with open(filename, 'r') as file:
        for line in file:
            line = int(line.strip())
            sumNumber += line
    return sumNumber 

def greatestNumber(filename):
    greatest = 1
    with open(filename, 'r') as file:
        for line in file:
            line = line.strip()
            line=int(line)
            if greatest < line:
                    greatest = line
    return greatest

def averageNumber(filename):
    average_Number = 0
    count = 0
    with open(filename, 'r') as file:
        for line in file:
            line = int(line.strip())
            average_Number += line
            count += 1
        average_Number = average_Number / count
        average_Number = float(f"{average_Number:.2f}")
    return average_Number
main()