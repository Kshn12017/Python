import random

def number_guessing_game():
    print("Welcome to the Number Guessing Game!")
    
    # Set the range for the number
    lower_bound = 1
    upper_bound = 100
    secret_number = random.randint(lower_bound, upper_bound)
    
    # Set the number of attempts
    attempts = 7
    
    print(f"I'm thinking of a number between {lower_bound} and {upper_bound}.")
    print(f"You have {attempts} attempts to guess the number.\n")
    
    for attempt in range(1, attempts + 1):
        guess = int(input(f"Attempt {attempt}: Enter your guess: "))
        
        if guess < secret_number:
            print("Too low!")
        elif guess > secret_number:
            print("Too high!")
        else:
            print(f"Congratulations! You guessed the number {secret_number} in {attempt} attempts.")
            break
    else:
        print(f"Sorry, you've used all {attempts} attempts. The number was {secret_number}.")
    
    # Ask if the player wants to play again
    play_again = input("Do you want to play again? (yes/no): ").strip().lower()
    if play_again == 'yes':
        number_guessing_game()
    else:
        print("Thanks for playing! Goodbye.")

if __name__ == "__main__":
    number_guessing_game()