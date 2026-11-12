LOWER_ALPHABETS = "abcdefghijklmnopqrstuvwxyz"
UPPER_ALPHABETS = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"


def main():
    print("Program starting.\n")
    rows = collectingWords()
    cipher = ciphering(rows)
    savingCipheredText(cipher)
    print("Program ending.")

def collectingWords():
    print("Collecting plain text rows for ciphering.")
    row = input("Insert row(empty stops): ")
    rows = ""
    while row != "":
        rows += row + "\n"
        row = input("Insert row(empty stops): ")
    
    return rows    


def ciphering(rows):
    print("\n#### Ciphered text ####")

    cipher = ""

    for row in rows.split("\n"):
        if row != "":
            cipherRow = ""

            for character in row:
                if character in LOWER_ALPHABETS:
                    position = LOWER_ALPHABETS.index(character)
                    newCharacter = LOWER_ALPHABETS[(position + 13) % 26]

                elif character in UPPER_ALPHABETS:
                    position = UPPER_ALPHABETS.index(character)
                    newCharacter = UPPER_ALPHABETS[(position + 13) % 26]

                else:
                    newCharacter = character

                cipherRow += newCharacter

            cipher += cipherRow + "\n"
    print(cipher)
    print("\n#### Ciphered text ####")
    return cipher

def savingCipheredText(cipher):
    filename = input("Insert filename to save: ")
    if filename == "\n" or filename == "":
        print("File name not defined.")
        print("Aborting save operation.")
    else:
        with open(filename, 'w') as file:
            file.write(cipher)
        print("Ciphered text saved!")

main()
