import random,time


def countdown():
    for i in range(3,0,-1):
        time.sleep(1)
        print(i)

    time.sleep(1)
    print("LETS ")

def exit():
    print("Game ending...")
    time.sleep(0.5)
    print(".")
    time.sleep(0.5)
    print("..")
    time.sleep(0.5)
    print("...")
    time.sleep(0.5)

def start():
    print("The game starts again...")
    time.sleep(0.5)
    startGame()

def startGame (numberOfPrediction=5):

    print("The game is about to begin...")
    countdown()
    print("Careful!! You only get 5 guesses")

    rightNumber = random.randint(0, 50)

    while (numberOfPrediction > 0):
        prediction = int(input("I kept a number between 0 and 50, go on, guess: "))
        if (prediction > rightNumber):
            print("The number you estimated is high, reduce it a little: ")
            numberOfPrediction -= 1
        elif (prediction < rightNumber):
            print("The number you're estimating is low, raise it a bit: ")
            numberOfPrediction -= 1
        else:
            print("**** Congratulations, you got the number right in my mind ****")
            print("The number I had in my mind was: " + str(rightNumber))
            break

    if (numberOfPrediction == 0):
        print("I'm sorry! Your guessing rights are over.")
        print("The number I had in my mind was: " + str(rightNumber))

    playAgain = input("Do you want to play again? Y/N: ")
    if (playAgain == "Y" or playAgain == "y"):
        startGame()
    elif (playAgain == "N" or playAgain == "n"):
        exit()
    else :
        print("Goodbye")
        exit()

startGame()