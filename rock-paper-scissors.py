import random

def game():
    while True:
        moves = {'rock':['paper','spock'],'paper':['scissors','lizard'],'scissors':['rock','spock'],'lizard':['rock','scissors'],'spock':['lizard','paper']}
        #list_of_moves = ['rock','paper','scissors','lizard','spock']

        player_one = input("Play: ").lower().strip()
        player_two = input("Play: ").lower().strip()
        #print(computer_moves) #to see which move the computer played

        if player_one == player_two:
            return 'Draw!!'

        if player_one in moves[player_two]:
            print('Player one wins!!!')
        else:
            print('Player two wins!!')

        play_again = input("Do you wnat to play again?(yes/no): ")
        if play_again.lower() != "yes":
            return "End of Game"

print(game())