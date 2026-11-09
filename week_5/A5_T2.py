def main():
    print("Program starting.")
    word=input("Insert word: ")
    print("")
    frameWord(word)
    print("\nProgram ending.")
    return None
def frameWord(word):
    print('*' * (len(word) + 4))
    print(f"* {word} *")
    print('*' * (len(word) + 4))
    return None
main()


