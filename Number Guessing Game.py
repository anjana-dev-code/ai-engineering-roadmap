import random

def play_game():
    secret_number = random.randint(1,100)
    attempts = 0
    guessed_correctly = False

    print("I am thinking of a number between 0 to 100.Guess it!")

    while not guessed_correctly:
        guess = input("Your guess: ")


    if not guess.isdigit():
        print("Please enter a valid number.")
        continue
         

    guess = int(guess)
    attempts += 1

    if guess < secret_number:
        print("Too low.")
    elif guess > secret_number:
        print("Too high.")
    else:
        print(f"Correct! You got it in {attempts} attempts.")
        guessed_correctly = True

if __name__ == "__main__":
    play_game()
     
           
