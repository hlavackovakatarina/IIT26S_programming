# NUMBER GUESSING GAME
import random
def main():
    print("NUMBER GUESSING GAME\nTRY TO GUESS THE NUMBER!\nThe range is 0 - 1000")
    attempts = 0 
    number = random.randint(0,1000) # the number needed to be guessed
   
    while attempts < 15:
        attempts += 1
        guesses = int(input("What number do you think is hiding? Take a guess: "))
        if guesses > 1000 or guesses < 0:
                    print("Guess within the range 0 - 1000")
        #HINTS
        if guesses > number:
            print ("The number is lower! Try again!")
        elif guesses < number:
            print ("The number is higher! Try again!")
        #Win
        elif guesses == number:
            print("YOU GUESSED THE NUMBER!!\nCONGRATULATIONS")
            print(f"It took you {attempts} attemps to find the number!")
            print(f"Number was {number} and you found {guesses}")
            break
    #Lost   
    if attempts == 15 and guesses != number:
            print("Sorry you did not guess the number...\n You can try it another time!")
            print(f"The number was {number}")

main()