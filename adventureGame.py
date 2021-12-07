import csv
import time
import sys
import os


def playGame(line):
    # Creating the story 2D list.
    story = []

    # Opening the story.
    storyInput = open("story.csv", "r")

    # Reading the CSV story.
    csvReader = csv.reader(storyInput)

    # Putting the CSV story into the 2D list.
    for row in csvReader:
        story.append(row)

    # Closing story file when done reading and writing to 2D list.
    storyInput.close()

    # Setting flag for while loop.
    gameOver = False

    # Plays the game if flag is false.
    while gameOver == False:

        # Printing out options to pick from when playing game.
        print(story[line][0])
        print("What do you want to do?")
        print("1 -",story[line][1])
        print("2 -",story[line][2])
        print("3 - Save Game")

        # Getting input from the user
        answer = input()

        # Picking option 1
        if (answer == "1"):
            line = int(story[line][3])
            line = line - 1
            
            # If the options are empty strings the flag changes to true and the while loop is over.
            if (story[line][2] == "" and story[line][3] == ""):
                print(story[line][0])
                gameOver = True
                time.sleep(2)

        # Picking option 2
        elif (answer == "2"):
            line = int(story[line][4])
            line = line - 1

            # If the options are empty strings the flag changes to true and the while loop is over.
            if (story[line][2] == "" and story[line][3] == ""):
                print(story[line][0])
                gameOver = True
                time.sleep(2)

        #Picking option 3
        elif (answer == "3"):
            saveGame = open("saved.txt", "r+")
            lines = saveGame.readlines()
            if (len(lines) != 0):
                del lines[0]
            saveGame.close()
            # Writing the line position for the save game to the saved.txt file.
            newSave = open("saved.txt", "w")
            lineSave = line
            newSave.write(str(lineSave))
            newSave.close()
            print("**** Game Saved ****")
        else:
            print("****** ERROR -- You must choose between the 3 options! ******")

    #print(line)
    

def getMenuInput():
    # getting input from user in the menu of the game.
    menuInput = input()

    if menuInput == "1":
        line = 0
        #print(line)
        return line 

    # Loading save game if exists.
    elif menuInput == "2":
        loadSaveGame = open("saved.txt", "r")
        line = loadSaveGame.readline()
        # If text file is empty sets the line to 0 to start from the begining and notifys user there was no saved game.
        if (line == ""):
            line = 0
            print("**** - There was no saved game detected -- Starting new game! - ****")
            return line
        # Adjusting the index so it starts at the right spot.
        line = int(line) - 1
        #print(line)
        return line

    # Quitting game if user wants to quit
    elif menuInput == "3":
        print("Too bad you don't want to play")
        print("**** - Quitting game - ****")
        return menuInput

    else:
        print("****** - ERROR -- You must choose between the 3 options - ******")
        initilizeGame()
        return getMenuInput()


def initilizeGame():

    # Initializing game and printing out menu option.
    print("****** Text Adventure Game v1.0 ******")
    print("*                                    *")
    print("*           1 - New Game             *")
    print("*           2 - Load Game            *")
    print("*           3 - Quit                 *")
    print("*                                    *")
    print("**************************************")

    #creating saved.txt file if it doesnt exist
    savegamecreate = open("saved.txt", "a")
    savegamecreate.close()

def main():
    # While loop to start game
    while True:
        initilizeGame()
        # gets menu input to start, quit, or load game.
        line = getMenuInput()
        # If user quits this ends the program.
        if (line == "3"):
            return
        # Plays game.
        playGame(line)

main()