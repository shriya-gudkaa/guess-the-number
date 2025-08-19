import random
import time

high_score = 0  

while True:
    num_guess = random.randint(1, 20)
    guess = None
    tries = 0
    max_score = 100
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
            print("You have guessed it right!", num_guess, "is the correct answer")

        if tries == 3 and guess != num_guess:
            if num_guess % 2 == 0:
                print("Hint: The number is even.")
            else:
                print("Hint: The number is odd.")

    end_time = time.time()
    total_time = end_time - start_time

    if guess == num_guess:
        score = max_score - (tries - 1) * 10 - int(total_time)
        if score < 0:
            score = 0
        print(f"Your score: {score}")

        if score > high_score:
            high_score = score
            print("Congratulations! You set a new high score!")
        else:
            print(f"The current high score is {high_score}")
    else:
        print("Better luck next time!")
        print(f"The correct number was: {num_guess}")
        print("Your score: 0")
        print(f"The current high score is {high_score}")

    print(f"You took {total_time:.2f} seconds to guess the number!")
    play_again = input("Do you want to play again? (y/n): ").lower()
    if play_again != 'y':
        print("Thanks for playing!")
        break
