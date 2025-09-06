secret_number = 7 # The number to be guessed
guess_count = 0 # Number of incorrect guesses
guess_limit = 3 # Maximum number of guesses allowed
while guess_count < guess_limit: # Loop until the user runs out of guesses
    guess= int(input('Guess: ')) # Get user input
    guess_count += 1 # Increment the guess count
    if guess == secret_number: # Check if the guess is correct
        print("You win!") 
        break # Exit the loop if the guess is correct
else:
    print("You lose!")
    print("The secret number was:", secret_number)