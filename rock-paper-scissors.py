import random

def game_play():    
    while True:
        player = input("Enter rock, paper, scissors: ")
        moves = ["rock","paper","scissors"]
        computer = random.choice(moves)

        if player == computer:
            print("It's a tie")
        elif player == "paper":
            if computer == "rock":
                print("paper covers rock, Paper wins!")
            else:
                print("Scissors cuts paper")
        elif player == "scissors":
            if computer == "paper":
                print("Scissors cuts paper")
            else:
                print("rock crushes scissors")
        elif player == "rock":
            if computer == "scissors":
                print("rock crushes scissors")
            else:
                print("paper covers rock")

        play_again = input("Do you wnat to play again? (yes/no): ")
        if play_again.lower() != "yes":
            break

game_play()
        

