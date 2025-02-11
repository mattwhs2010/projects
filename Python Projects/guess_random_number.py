# This is a Python program that i've created for user input,random number generation, while loops,if statements and data validation#

import random

def get_user_name_and_player_choice(): # Creation of function to get user name and play choice #
    user_name = input("Hello- what is your name? ") # Asking for user name #
    print(f"Welcome, {user_name}!") # Welcoming user #
    while True:  # Creation of a while loop to see if the user wants to play the game #
        player_choice = input(f"{user_name}, would you like to play a game? (yes/no): ").lower().strip() # asking user if they want to play the game#
        if player_choice =="yes":
            return user_name, True  # Returning user name and true if user wants to play the game #
        elif player_choice == "no":
            return user_name, False # Returning user name and false if user does not want to play the game #
        else:
            print("Invalid input. Please enter yes or no.")


def get_user_guess(): # Creation of function to get user guess #
    while True: # Creation of while loop to validate user input #   
        try:
            user_guess = int(input("Guess a number between 1 and 5: ")) # Asking user to guess a number between 1 and 5 #
            if 1 <= user_guess <= 5: # If user guess is between 1 and 5, return user guess #
                return user_guess
            else:
                print("Your guess is out of range. Please try again. You need to provide a number between 1 and 5.")
        except ValueError:
            print("Invalid input. Please enter a number between 1 and 5.")


def random_number_game(user_name):
    random_number = random.randint(1, 5) # Generating a random number between 1 and 5 #
    user_guess_count = 0

    while True: 
        user_guess = get_user_guess() # Calling function to get user guess #
        user_guess_count += 1
    
        if user_guess == random_number:
            print(f"Congratulations {user_name}! You guessed {random_number} in {user_guess_count} tries!")
            break
        elif user_guess < random_number:
            print("Too low! Try again.")
        else:
            print("Too high! Try again.")

# Main game execution
name, wants_to_play = get_user_name_and_player_choice()
if wants_to_play:
    print(f"Let's play, {name}!")
    random_number_game(name)
else:
    print(f"Maybe next time, {name}!")  

        
    
 

  




