import random
import time

num_guess = random.randint(1, 20)
guess = None
tries = 0

print("Welcome to the guess the number game!")
start_time = time.time()

while guess != num_guess and tries < 5:
    guess = int(input("Enter your guess: "))
    tries += 1
    
    if guess > num_guess:
        print("Too high")
    elif guess < num_guess:
        print("Too low")
    else:
        print("you have guessed it right",num_guess,"is the correct answer")
    if tries == 3 and guess != num_guess:
        if num_guess % 2 == 0:
            print("Hint: The number is even.")
        else:
            print("Hint: The number is odd.")

    if tries == 5 and guess != num_guess:
        if num_guess % 3 == 0:
            print("Hint: The number is a multiple of 3.")
        elif num_guess % 5 == 0:
            print("Hint: The number is a multiple of 5.")
        else:
            print("Hint: The number is not a multiple of 3 or 5.")
end_time = time.time()
total_time = end_time - start_time


if guess != num_guess:
    print("Better luck next time!")
    print(f"The correct number was: {num_guess}")
print(f"You took {total_time:.2f} seconds to guess the number!")

