def report(names, shortest_name, longest_name, avarage_name):
    print("#### REPORT BEGIN ####")
    print(f"Name count: - {names}")
    print(f"Shortest name: - {shortest_name} chars")
    print(f"Longest name: - {longest_name} chars")
    print(f"Average name length: - {avarage_name} chars")
    print("#### REPORT END ####")

def shortest(filename):
    shortest_name = 0
    with open(filename, 'r') as file:
        for line in file:
            name = line.strip()
            if name != '':
                if shortest_name == 0 or shortest_name > len(name):
                    shortest_name = len(name)
    return shortest_name
def longest(filename):
    longest_name = 0
    with open(filename, 'r') as file:
        for line in file:
            name = line.strip()
            if longest_name==0 or longest_name < len(name):
                longest_name = len(name)
    return longest_name
def avarage(filename):
    avarage_name= 0
    total_names = 0
    with open(filename, 'r') as file:
        for line in file:
            name = line.strip()
            if name != '':
                total_names += 1
                avarage_name += len(name)
        avarage_name = avarage_name / total_names
        avarage_name = float(f"{avarage_name:.2f}")
    return avarage_name

def readFile(filename):
    names = 0
    print(f"Reading names from \"{filename}\".")
    with open(filename, 'r') as file:
        for line in file:
            line = line.strip()
            names += 1
            if line == '':
                names -= 1
    print("Analysing names...")
    print("Analysis complete!")
    return names
def main():
    print("Program starting.")
    print("This program analyses a list of names from a file.")
    filename = input ("Insert filename to read: ")
    names = readFile(filename)
    shortest_name = shortest(filename)
    longest_name = longest(filename)
    avarage_name = avarage(filename)
    report(names, shortest_name, longest_name, avarage_name)
    print("Program ending.")
main()
