DELIMITER = ","
def collectWords():
    words=""
    while True:
        word = input("Insert word (empty stops): ")
        if word == "":
            break
        else:
            if words == "":
                words = word
            else:
                words += DELIMITER + word
    return words
def analyseWords(words):
    list = words.split(DELIMITER)
    count=len(list)
    print(f" - {count} Words")
    characters = 0
    for word in list:
        characters += len(word)
    print(f" - {characters} Characters")
    avarage = characters / count
    print("- {:.2f} Average word length".format(avarage))
def main ():
    print("Program starting.") 
    collect = collectWords()
    analyseWords(collect)
    print("Program ending.")
    return None
main()               