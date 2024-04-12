import random
import time

def play_auto_guessing_game():
    target_number = random.randint(1, 100)  # Generate a random target number
    print(f"Target number: {target_number}")

    min_guess, max_guess = 1, 100  # Initial guess range

    while True:
        guess = random.randint(min_guess, max_guess)  # AI's guess
        print(f"AI guesses: {guess}")
        time.sleep(1)  # Pause for readability

        if guess < target_number:
            print("AI's guess is too low!")
            min_guess = guess + 1  # Adjust minimum guess range
        elif guess > target_number:
            print("AI's guess is too high!")
            max_guess = guess - 1  # Adjust maximum guess range
        else:
            print("AI guessed the correct number!")
            break

