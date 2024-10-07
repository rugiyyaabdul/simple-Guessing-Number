import random

def guess_number():
    number_to_guess = random.randint(1, 100)
    attempts = 0

    print("Welcome to the Guessing Game!")
    print("I’ve picked a number between 1 and 100. Can you guess what it is?")

    while True:
        try:
            guess = int(input("Your guess: "))
            attempts += 1

            if guess < number_to_guess:
                print(f"Too low! Try a number between {guess} and 100.")
            elif guess > number_to_guess:
                print(f"Too high! Aim for something between 1 and {guess}.")
            else:
                print(f"Great job! You guessed it in {attempts} attempts.")
                break
        except ValueError:
            print("Oops, that doesn’t seem like a number. Please try again.")

guess_number()
