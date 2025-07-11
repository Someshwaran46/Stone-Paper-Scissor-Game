import random

print("*********************************\n")
print("WELCOME TO THE STONE-PAPER-SCISSOR GAME !!")
print("MODE : Computer against Player")
print("\n*********************************\n")

# Player's turn
play1 = input("Player's turn: select any one (stone / paper / scissor): ")
player = play1.strip().lower()

# Computer's turn
print("Computer's turn: stone / paper / scissor")
computer_choice = random.randint(1, 3)

if computer_choice == 1:
    computer = 'stone'
elif computer_choice == 2:
    computer = 'paper'
elif computer_choice == 3:
    computer = 'scissor'

print("The computer has chosen.\n")

# Defining the game function
def sps_game(computer, player):
    if computer == player:
        return None  # Tie

    elif computer == 'stone':
        if player == 'scissor':
            return False
        elif player == 'paper':
            return True

    elif computer == 'paper':
        if player == 'stone':
            return False
        elif player == 'scissor':
            return True

    elif computer == 'scissor':
        if player == 'paper':
            return False
        elif player == 'stone':
            return True
        
result = sps_game(computer, player)

print("\n************************************\n")
print(f"The value selected by the computer is : {computer}")
print(f"The value selected by the player is : {player}")
print("\n*************************************\n")

# Declaring the result
if result is None:
    print("⚖️ It's a tie! Great minds think alike. 🤝")
elif result:
    print("🎉 You win! 🏆 Stone-Paper-Scissor Champion! 💪")
else:
    print("😞 You lose this round... Don't give up, try again! 🔄")

print("\n*************************************")


