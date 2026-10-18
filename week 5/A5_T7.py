def main():
    print("Program starting.")
    list = []
    number=[]
    while True:
        word = input("Insert word (empty stops): ")
        if word == "":
            break
        else:
            list.append(word)
            number.append(len(word))
    print(f"- {(len(list))} words")
    print(f"- {(sum(number))} characters")
    print(f"- {(sum(number)/len(number)):.2f} Average word length")
    print("\nProgram ending.")
    return None
main()

