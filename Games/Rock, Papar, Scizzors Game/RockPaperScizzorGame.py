from random import choice

ROCK = 'r'
PAPER = 'p'
SCIZZOR = 's'

emojis = {ROCK :'🗿', PAPER:'📄', SCIZZOR:'✂'}
choices = tuple(emojis.keys())


def get_user_choice():
    while True:
        userchoice = input("Enter your choice (r, p ,s): ").lower()
        if userchoice in choices:
            return userchoice
        else:
            print("Invalid choice!")


def display_choices(user_choice, computer_choice):
    print("You choice:", emojis[user_choice])
    print("Computer choice: ", emojis[computer_choice])



def play_game():
    games_played = 0
    user_wins = 0
    computer_wins = 0
    draws = 0
    while True:
        user_win_count = 0
        computer_win_count = 0
        for i in range(3):
            user_choice = get_user_choice()

            computer_choice = choice(choices)

            display_choices(user_choice, computer_choice)

            if user_choice == computer_choice:
                print("Draw\n")
            elif (
                    (user_choice == ROCK and computer_choice == PAPER) or
                    (user_choice == PAPER and computer_choice == SCIZZOR) or
                    (user_choice == SCIZZOR and computer_choice == ROCK)
            ):
                print("Computer won!\n")
                computer_win_count += 1
            else:
                print("You won!\n")
                user_win_count += 1


        if user_win_count > computer_win_count:
            games_played += 1
            user_wins += 1
            print("Overall You Won\n")
        elif user_win_count < computer_win_count:
            games_played += 1
            computer_wins += 1
            print("Overall Computer Won\n")
        elif user_win_count == computer_win_count:
            games_played += 1
            draws += 1
            print("Overall Draw\n")

        continue_playing = input("Would you like to play again? (y/n): ").lower()
        if continue_playing == 'n':
            print("Thank you for playing!")
            print(f'''
Total games played: {games_played}
You won {user_wins} times
Computer won {computer_wins} times
No of ties: {draws}
''')
            break


play_game()