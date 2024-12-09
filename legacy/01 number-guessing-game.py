import random

startNum = int(input("Enter starting number: "))
endNum = int(input("Enter ending number: "))

randNum = random.randint(startNum, endNum)

guessNum = int(input(f"Guess a number between {startNum} and {endNum}: "))

if guessNum == randNum:
    print("Congratulations! You guessed the correct number.")
else:
    print("Sorry, the correct number was", randNum)