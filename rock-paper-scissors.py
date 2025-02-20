import random

def game():
    while True:
        moves = {'rock':['paper','spock'],'paper':['scissors','lizard'],'scissors':['rock','spock'],'lizard':['rock','scissors'],'spock':['lizard','paper']}
        list_of_moves = ['rock','paper','scissors','lizard','spock']

        computer_one_moves = random.choice(list_of_moves)
        computer_two_moves = random.choice(list_of_moves)
        #print(computer_moves) #to see which move the computer played

        if computer_one_moves == computer_two_moves:
            return 'Draw!!'

        if computer_one_moves in moves[computer_two_moves]:
            print('Computer one wins')
        else:
            print('Computer two wins!!')

        play_again = input("Do you wnat to play again?(yes/no): ")
        if play_again.lower() != "yes":
            return "End of Game"

print(game())