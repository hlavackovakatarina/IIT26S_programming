def palindrome (win):
    phrase=input("Enter a phrase: ").lower()
    phrase1=''
    character=0
    for i in range(len(phrase)):
        if phrase[i] != ' ':
            phrase1+=phrase[i]
        character+=1
    phrase2=phrase1[::-1]
    print(f"Your phrase is: {phrase}")
    print(f"Your phrase without spaces is: {phrase1}")
    print(f"Your phrase backwards is: {phrase2}")
    if phrase1 == phrase2:
        print("Your phrase is a palindrome!")
        win += 1
    else:
        print('The phrase is not a palindrome!')
    print(f"Your phrase has {character} characters")
    print(f"The sentence has {len(phrase1)} characters without spaces")
    return win
def main():
    play = input("Do you want to check if a phrase is a palindrome? (yes/no): ")
    win = 0
    while play == 'yes':
        win = palindrome(win)
        play = input("Want to play again? (yes/no): ")
    else:
        print("Oh maybe next time!")
        print(f"{win} phrases were palindromes!")
main()