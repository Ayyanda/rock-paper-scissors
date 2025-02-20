import random

def game():
    while True:
        moves = {'rock':['paper','spock'],'paper':['scissors','lizard'],'scissors':['rock','spock'],'lizard':['rock','scissors'],'spock':['lizard','paper']}
        list_of_moves = ['rock','paper','scissors','lizard','spock']

        user_moves = input("Play: ")
        computer_moves = random.choice(list_of_moves)
        print(computer_moves) #to see which move the computer played

        if computer_moves == user_moves:
            return 'Draw!!'

        if computer_moves in moves[user_moves]:
            print('Computer wins')
        else:
            print('User wins!!')

        play_again = input("Do you wnat to play again?(yes/no): ")
        if play_again.lower() != "yes":
            return "End of Game"

print(game())