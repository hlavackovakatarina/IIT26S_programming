print("Program starting.\n")
list = []
number=[]
while True:
    word = input("Insert word (empty stops): ")
    list.append(word)
    number.append(len(word))
    if word =="" or word == "\n":
        break
print("\nYou inserted: ")
print("-",len(list)-1, "words")
print("-",sum(number), "characters")
print("\nProgram ending.")
