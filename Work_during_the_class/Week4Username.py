users=["Alice", "Bob", "Charlie", "David", "Eve", "Frank"]
name=input("\nEnter your name: ")
for i in range(3):
    if name in users:
        print("Welcome, " + name + "!")
        break
    if name not in users:
        print("Sorry, " + name + ", is not here.")   
        if i < 2:
            name=input("\nEnter your name: ")
        if i == 2:   
            print("\nSorry ,you are now locked out, you tried logging in 3 times.")
        