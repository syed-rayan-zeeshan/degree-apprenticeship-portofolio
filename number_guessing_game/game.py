import random



print("Welcome to the Number Guessing Game!")



number_to_guess = random.randint(1, 20)

attempts = 0



while True:

    guess = input("Guess a number between 1 and 20: ")

    

    if not guess.isdigit():

        print("Please enter a number.")

        continue

    

    guess = int(guess)

    attempts += 1

    

    if guess < number_to_guess:

        print("Too low! Try again.")

    elif guess > number_to_guess:

        print("Too high! Try again.")

    else:

        print(f"Correct! You guessed the number in {attempts} attempts.")

        break

