import random

print("\t\t\t\t\tSnake, Water, Gun Game\n\n")
print("Enter:\n's' for Snake\n'w' for Water\n'g' for Gun")

gameList = ['s', 'w', 'g']

computerScore = 0
userScore = 0
noOfChances = 0
def game(noOfChances):
    global userScore, computerScore
    while noOfChances <= 5:
        userInput = input("Snake (s), Water (w), Gun (g):\n>>>")
        computerInput = random.choice(gameList)

        if(userInput == computerInput):
            print("There's a tie. None gets a point!")

        elif(userInput == 's' and computerInput == 'w'):
            userScore += 1
            print(
                f"\nYou guessed: {userInput}\t\tComputer guessed: {computerInput}")
            print("You win a point!")
            print(f"Your Score: {userScore}\nComputer Score: {computerScore}")

        elif(userInput == 's' and computerInput == 'g'):
            computerScore += 1
            print(
                f"\nYou guessed: {userInput}\t\tComputer guessed: {computerInput}")
            print("Computer wins a point!")
            print(f"Your Score: {userScore}\nComputer Score: {computerScore}")

        elif(userInput == 'w' and computerInput == 's'):
            computerScore += 1
            print(
                f"\nYou guessed: {userInput}\t\tComputer guessed: {computerInput}")
            print("Computer wins a point!")
            print(f"Your Score: {userScore}\nComputer Score: {computerScore}")

        elif(userInput == 'w' and computerInput == 'g'):
            userScore += 1
            print(
                f"\nYou guessed: {userInput}\t\tComputer guessed: {computerInput}")
            print("You win a point!")
            print(f"Your Score: {userScore}\nComputer Score: {computerScore}")

        elif(userInput == 'g' and computerInput == 's'):
            userScore += 1
            print(
                f"\nYou guessed: {userInput}\t\tComputer guessed: {computerInput}")
            print("You win a point!")
            print(f"Your Score: {userScore}\nComputer Score: {computerScore}")

        elif(userInput == 'g' and computerInput == 'w'):
            computerScore += 1
            print(
                f"\nYou guessed: {userInput}\t\tComputer guessed: {computerInput}")
            print("Computer wins a point!")
            print(f"Your Score: {userScore}\nComputer Score: {computerScore}")

        else:
            print("Invalid input!\n")

        print(f"{5 - noOfChances} chances left out of 5\n")
        noOfChances += 1

game(noOfChances)

if(userScore == computerScore):
    print("Tie!")
elif(userScore > computerScore):
    print("You Won!")
else:
    print("Computer Won!")

print(f"Your final score: {userScore}\nComputer's final score: {computerScore}")