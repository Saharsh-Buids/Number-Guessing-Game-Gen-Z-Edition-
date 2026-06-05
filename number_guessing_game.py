import random

# The main game loop.
while True:
    # This Print Statement is to leave SPACE!!when the user repalys the game! (yes, again)

    print()

    # DECLARING THE NUMBERS FOR EACH DIFFICULTY LEVEL.
    number_easy = random.randint(1, 100)
    number_medium = random.randint(1, 500)
    number_hard = random.randint(1, 1000)

    attempts = 0  # this tracks no. of attempts.

    # introduction and difficulty selection.
    print("Welcome to the Number Guessing Game!\n")
    print("Choose your difficulty level:\n")
    print("1. Easy (1-100)")
    print("2. Medium (1-500)")
    print("3. Hard (1-1000)\n")

    #asking the user to select a difficulty level!
    difficulty = input("Enter your difficulty level (1-3): ")

    #defining the number to guess based on the user's choice!
    if difficulty == "1":
        number = number_easy
        print("\nCan you Guess the number between 1 and 100? (EASY MODE)")
    elif difficulty == "2":
        number = number_medium
        print("\nCan you Guess the number between 1 and 500? (MEDIUM MODE)")
    elif difficulty == "3":
        number = number_hard
        print("\nCan you Guess the number between 1 and 1000? (HARD MODE)")
    #if the user enters an invalid difficulty level, we will default to HARD mode!
    else:
        print("\nInvalid difficulty level! You're going to HARD mode!!")
        number = number_hard
        print("\nCan you Guess the number between 1 and 1000? (HARD MODE) since you entered an invalid difficulty level..(Muhaaha)")

    # The guessing loop.
    while True:
        #if they enter an invalid guess, we ROAST THEM!!
        guess = input("\nEnter your guess bro!: ")
        if not guess.isdigit(): #just learned about isdigit() !!
            print("blud can't even type a valid number!")
            continue
        
        guess = int(guess) #typecasting
        attempts = attempts + 1 #INcrementing attempts!

        #the Comparison of the guess with the actual number!
        if guess < number:
            print("Too low dude.")
        elif guess > number:
            print("Too high dude.")
        
        #if the user WINS, we will congratulate them and break out of the Gessing Loop!
        else:
            print(f"\n\nCertified Number Rizzler🗿 You guessed it in {attempts} attempts.\n")
            print(f"The number was {number} btw.\n")
            break 
            #we break out of the guessing loop to the Main game loop!!

    #replay option!
    replay = input("Wanna play again? (y/n): ")
    if replay.lower() != "y" and replay.lower() != "yes":
        break #Breaks out of the main game loop to end the game!
    if replay.lower() == 'y' or replay.lower() == "yes":
        print() #space for better readability
        continue #continue with the loop to replay the game!

print("\nThanks for playing the Number Guessing Game! See you next time!\n")



#made by #Saharsh_builds! 

#love you all!! <3