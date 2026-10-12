print("Program starting,")
word=input("Insert word (empty stops): ")
word_count=0
CharCount=0
while word !="":
    print("yey, I'm in the loop")
    word_count += 1
    CharCount += len(word)
print("You inserted:")
print(f"- {word_count} words")
print(f"- {CharCount} characters")
print("Program ending.")

