import random
target = random.randint(1, 10)

while True:
    userChoice = input("Guess the target or Quit (Q): ")

    if userChoice == "Q":
        print("You quit the game. Goodbye!")
        break

    # Only convert to int if it's not Q
    try:
        userChoice = int(userChoice)
    except ValueError:
        print("Invalid input! Please enter a number or 'Q' to quit.")
        continue

    if userChoice == target:
        print("🎉 Congratulations! You guessed the number!")
        break
    elif userChoice < target:
        print("Too small! Try a bigger number...")
    else:
        print("Too high! Try a smaller number...")

print("-------GAME OVER------")
