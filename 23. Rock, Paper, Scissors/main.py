import random

choices = ["rock", "paper", "scissors"]
player_score = 0
computer_score = 0

def get_player_choice():
    answer = input("Your choice ('q' for quit):[rock, paper, scissors]").lower()
    return answer

def decide_winner(player, computer):
    if player == computer:
        return "draw"
    elif player == "rock" and computer == "scissors":
        return "player"
    elif player == "scissors" and computer == "paper":
        return "player"
    elif player == "paper" and computer == "rock":
            return "player"
    else:
         return "computer"

if __name__ == "__main__":
    while True:
        choice = get_player_choice()
        if choice.lower() == "q":
            print("Thanks for playing!")
            break

        if choice not in choices:
            print("Invalid Choice.")
            continue
        
        computer = random.choice(choices)
        win = decide_winner(choice, computer)

        print(f"Player chose: {choice}")
        print(f"Computer chose: {computer}")

        if win == "player":
            player_score += 1
            print(f"You win! Player: {player_score} Computer: {computer_score}")
        elif win == "computer":
            computer_score += 1
            print(f"Computer win! Player: {player_score} Computer: {computer_score}")
        else:
            print(f"Draw!, Player:{player_score} and Computer: {computer_score} ")

        if player_score == 3:
            print("Player Win!!!")
            print("Game Over.")
            play_again = input("Play again? (y/n): ")
            if play_again.lower() == "y":
                player_score = 0
                computer_score = 0
                continue
            elif play_again.lower() == "n":
                break
            else:
                print("Invalid Answer.")
                break

        if computer_score == 3:
            print("Computer Win!!!")
            print("Game Over.")
            play_again = input("Play again? (y/n): ")
            if play_again.lower() == "y":
                player_score = 0
                computer_score = 0
                continue
            elif play_again.lower() == "n":
                break
            else:
                print("Invalid Answer.")
                break
        
         