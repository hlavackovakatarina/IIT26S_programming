#Game guess the game correctly
correct_number = 23
while True:
 guess = int(input("Enter an integer: "))
 if guess == correct_number:
    print("You guessed correctly!")
    print("Game ends here")
    break
 elif guess < correct_number:
    print("The number is higher than your guess")
 else:
    print("The number is lower than your guess")
print("This prints at the end, after the while loop.")

# File: for.py
for i in range(1, 5):
    print(i)
print("Loop has ended.")