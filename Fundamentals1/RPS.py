import random
# returns a random number between 1 and 3 inclusive

def get_random_choice():
    pass


# returns a text choice based on a number choice (Rock-1, Paper-2, Scissors-3)
def get_text_choice(num_choice):
    pass

# returns the computer's choice in text format
def get_computer_choice():
    pass

# returns the player choice based on num_choice

def get_player_choice(num_choice):
    pass
# returns the winner
def get_winner(player, computer):
    pass

# plays a single game and allows for user input to enter a choice
def play_a_game():
    pc = int(input("Enter your choice: "))
    player = get_player_choice(pc)
    computer = get_computer_choice()
    print("Player choice:", player)
    print("Computer choice:", computer)
    print(get_winner(player, computer))


# allows for user input to play multiple games
def main():
    play_again = "y"
    while  True:
        while play_again == "y":
            #play_a_game()
            play_again = input("Play again? (y/n): ")

# Start the game
main()