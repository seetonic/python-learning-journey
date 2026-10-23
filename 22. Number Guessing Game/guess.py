import random

secret = random.randint(1, 10)
tries = 0

def ask_guess():
    answer = int(input("Guess a number (1 - 10) "))
    return answer

if __name__ == "__main__":
    while True:
        guess = ask_guess()
        tries += 1

        if guess == secret:
            print("You win! Tries:", tries)
        elif guess < secret:
            print("Too low")
        else:
            print("Too high")

        if guess == secret or tries == 5:
            if tries == 5 and guess != secret:
                print("You lose! Tries:", tries)

            play_again = input("Play again? (y/n): ").lower()
            if play_again == "y":
                secret = random.randint(1,10)
                tries = 0
                continue
            elif play_again == "n":
                print("Thanks for playing!")
                break
            else:
                print("invalid Input")
                continue