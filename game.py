import random
def play_game():
    number_to_guess = random.randint(1,45)
    max_attempts = 15
    attempts = 0

    print("\n Welcome to the Number Guessing Game!")
    print("Guess the number (it's between 1 and 45). You only have 3 chances!")

    while attempts < max_attempts:
        try:
            guess = int(input(f"Attempt {attempts + 1}: Enter your guess: "))
            attempts += 1

            if guess == number_to_guess:
                print(f" Correct! You guessed the number in {attempts} attempt(s).")
                break
            elif guess < number_to_guess:
                print("Too low!")
            else:
                print("Too high!")

        except ValueError:
            print(" Please enter a valid number.")

    if attempts == max_attempts and guess != number_to_guess:
        print(f" Out of attempts! The correct number was {number_to_guess}.")

# Main game loop
while True:
    play_game()
    choice = input("\nDo you want to play again? (yes/no): ").strip().lower()
    if choice != 'yes':
        print(" Thanks for playing! Goodbye!")
        break
