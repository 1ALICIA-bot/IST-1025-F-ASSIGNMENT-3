import random

def stone_knife_paper():
    choices = ['S', 'K', 'P']  # S = Stone, K = Knife, P = Paper
    user_choice = input("Enter your choice (S for Stone, K for Knife, P for Paper): ").upper()

    if user_choice not in choices:
        print("Invalid choice! Please enter S, K, or P.")
        return

    computer_choice = random.choice(choices)
    print(f"Computer chose: {computer_choice}")

    if user_choice == computer_choice:
        print("It's a tie!")
    elif (user_choice == 'S' and computer_choice == 'K') or \
         (user_choice == 'K' and computer_choice == 'P') or \
         (user_choice == 'P' and computer_choice == 'S'):
        print("You win!")
    else:
        print("Computer wins!")

stone_knife_paper()
