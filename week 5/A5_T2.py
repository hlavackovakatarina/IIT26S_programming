def main():
    print("Program starting.")
    word=input("Insert word: ")
    frameWord(word)
def frameWord(word):
    print("*" * len(word) + 2)
    print(f"*{word}*")
    print("*" * len(word) + 2)
main()


