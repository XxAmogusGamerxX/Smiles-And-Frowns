import random
import time
import os


def clearConsole():
  command = 'clear'
  if os.name in ('nt', 'dos'):  # If Machine is running on Windows, use cls
    command = 'cls'
  os.system(command)


firstTime = True
difficulty = ""
playing = True
while (playing == True):
  difficulty2 = str(
    input(
      "What difficulty do you want? Input the number next to the difficulty.\n\n- (1) Easy \n  - 3 seconds\n\n- (2) Medium\n  - 2 seconds\n\n- (3) Hard\n  - 1 second\n\n- (4) Expert\n  - 0.5 seconds\n\n- (5) Extreme\n  - 0.2 seconds\n\n- (6) Impossible \n  - 0.05 seconds\n  - no grid numbers\n\n"
    ))

  if (difficulty2 == "1"):
    difficulty = "easy"
  elif (difficulty2 == "2"):
    difficulty = "med"
  elif (difficulty2 == "3"):
    difficulty = "hard"
  elif (difficulty2 == "4"):
    difficulty = "impos"
  elif (difficulty2 == "5"):
    difficulty = "extreme"
  elif (difficulty2 == "6"):
    difficulty = "expert"

  currTime = 0
  numbFrown = random.randint(1, 25)
  grid = [["", "", "", "", ""], ["", "", "", "", ""], ["", "", "", "", ""],
          ["", "", "", "", ""], ["", "", "", "", ""]]
  currNumb = 0
  indexFinal = ""

  for i1 in range(5):
    for i2 in range(5):
      currNumb += 1
      if (currNumb != numbFrown):
        grid[i1][i2] = ":)"
      else:
        grid[i1][i2] = ":("
        indexFinal = f"{i2 + 1},{i1 + 1}"

  final = ""
  for i3 in range(5):
    if (difficulty != "expert"):
      final += str(i3 + 1) + " -- "
    for i4 in range(5):
      final += grid[i3][i4] + " "
    final += "\n"

  clearConsole()

  if (firstTime == True):
    tutor = input("Do you want the tutorial? Yes to see or enter to skip. \n")
    if (tutor == "Yes"):
      input(
        "You will be prompted with a 5x5 board of smiley faces and you have to find the frowny face's coordinates before the timer runs out. The coordinates are in the (x,y or xy) form. Good Luck!\n"
      )

  clearConsole()

  input("Press enter to start.\n")

  if (difficulty == "hard"):
    for i in range(10):
      clearConsole()
      currTime += 0.1
      currTime = round(currTime, 1)
      print(currTime)
      if (difficulty != "expert"):
        print(final + "     |  |  |  |  |\n     1  2  3  4  5")
      print("DO NOT ANSWER YET!")

      time.sleep(0.1)
  if (difficulty == "easy"):
    for i in range(30):
      clearConsole()
      currTime += 0.1
      currTime = round(currTime, 1)
      print(currTime)
      if (difficulty != "expert"):
        print(final + "     |  |  |  |  |\n     1  2  3  4  5")
      print("DO NOT ANSWER YET!")

      time.sleep(0.1)
  if (difficulty == "extreme"):
    for i in range(2):
      clearConsole()
      currTime += 0.1
      currTime = round(currTime, 1)
      print(currTime)
      if (difficulty != "expert"):
        print(final + "     |  |  |  |  |\n     1  2  3  4  5")
      print("DO NOT ANSWER YET!")

      time.sleep(0.1)

  if (difficulty == "med"):
    for i in range(20):
      clearConsole()
      currTime += 0.1
      currTime = round(currTime, 1)
      print(currTime)
      if (difficulty != "expert"):
        print(final + "     |  |  |  |  |\n     1  2  3  4  5")
      print("DO NOT ANSWER YET!")

      time.sleep(0.1)
  if (difficulty == "impos"):
    for i in range(5):
      clearConsole()
      currTime += 0.1
      currTime = round(currTime, 1)
      print(currTime)
      if (difficulty != "expert"):
        print(final + "     |  |  |  |  |\n     1  2  3  4  5")
      print("DO NOT ANSWER YET!")

      time.sleep(0.1)
  if (difficulty == "expert"):
    for i in range(1):
      clearConsole()
      currTime += 0.05
      currTime = round(currTime, 1)
      print(currTime)
      print(final)
      print("DO NOT ANSWER YET!")

      time.sleep(0.05)
  clearConsole()

  numbGuessQuest = input(
    "What coordinate was the frowny face located at? In the (x,y or xy) format. examples: 3,2 or 32\n"
  )
  foundGuess = False
  if (numbGuessQuest != ""):
    for i in range(len(numbGuessQuest)):
      if (numbGuessQuest[i] == ","):
        foundGuess = True
    if (foundGuess == False):
      numbGuess = str(numbGuessQuest[0]) + "," + str(numbGuessQuest[1])
    else:
      numbGuess = numbGuessQuest
  else:
    numbGuess = numbGuessQuest
  clearConsole()
  if (numbGuess == indexFinal):
    print("You won!")
    print(f"  -The answer was: {indexFinal}.\n  -You guessed: {numbGuess}.\n")
  else:
    print("You lost!")
    print(f"  -The answer was: {indexFinal}.\n  -You guessed: {numbGuess}.\n")

  contin = input("Do you want to continue? y/n \n")
  if (contin == "n"):
    playing = False
    clearConsole()
  firstTime = False
  clearConsole()
