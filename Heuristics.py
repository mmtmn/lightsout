# made by Thiago M Nóbrega
# to run this project: python main.py

import numpy as np
from game5x5 import play
from translator5x5 import translate

print("")
print("1 - First open the following website on your browser of choice:") 
print("https://www.geogebra.org/m/JexnDJpt#material/RmRUx8Yd")
print("")
print("We will be solving a 5 by 5 lights out puzzle")
print("2 - First click on the button 'restart' and than on 'random'.")
print("3 - Next, please enter the inputs of each row")
print("4 - 1 is equal to a light on, and a zero is equal to a light off")
print("5 - There should be 5 numbers per row.")
print("6 - Please enter each of the inputs of the lights out game and separate them by a space, when finished, please press enter...")

def HeuristicsResolution():
    """ Main function of the software
    """
    # collecting input for inicial space's position
    # collecting row1's inputs
    row1 = list(map(int, input("row #1: ").split()))
    # making sure row have 5 digits
    while len(row1) != 5:
        row1.clear()
        row1 = list(map(int, input("row #1: ").split()))
    # making sure digits are either zero or one
    if len(row1) == 5:
        for x in row1:
            if x != 1 and x != 0:
                row1.clear()
                row1 = list(map(int, input("row #1: ").split()))
    # collecting row2's inputs
    row2 = list(map(int, input("row #2: ").split()))
    while len(row2) != 5:
        row2.clear()
        row2 = list(map(int, input("row #2: ").split()))
    if len(row2) == 5:
        for x in row2:
            if x != 1 and x != 0:
                row2.clear()
                row2 = list(map(int, input("row #2: ").split()))
    # collecting row3's inputs
    row3 = list(map(int, input("row #3: ").split()))
    while len(row3) != 5:
        row3.clear()
        row3 = list(map(int, input("row #3: ").split()))
    if len(row3) == 5:
        for x in row3:
            if x != 1 and x != 0:
                row3.clear()
                row3 = list(map(int, input("row #3: ").split()))
    # collecting row4's inputs
    row4 = list(map(int, input("row #4: ").split()))
    while len(row4) != 5:
        row4.clear()
        row4 = list(map(int, input("row #4: ").split()))
    if len(row4) == 5:
        for x in row4:
            if x != 1 and x != 0:
                row4.clear()
                row4 = list(map(int, input("row #4: ").split()))
    # collecting row5's inputs
    row5 = list(map(int, input("row #5: ").split()))
    while len(row5) != 5:
        row5.clear()
        row5 = list(map(int, input("row #5: ").split()))
    if len(row5) == 5:
        for x in row5:
            if x != 1 and x != 0:
                row5.clear()
                row5 = list(map(int, input("row #5: ").split()))
    # all the data was collected for the inicial spacial state
    rows = [row1,row2,row3,row4,row5]
    # turning the rows into a 5x5 numpy array
    game = np.array(rows)
    # list that carries over all operations for final response
    final_solution = []
    print(game)
    # variable that makes sure the game is not impossible
    impossible = 0
    # important while loop that ends when game is resolved
    while np.count_nonzero(game) and impossible != 100:
        impossible += 1
        # list to keep track of row's solutions and game's next steps
        row1_solution = []
        # keeps track of which special state is being validated
        location = 0
        for x in game:
            # if the light is on
            for y in x:
                location += 1
                if y == 1:
                    # on the first row
                    if location < 6:
                        row1_solution.append(location + 5)
                        final_solution.append(location + 5) 
        print("")
        print("The order you should click the lights is: ", row1_solution)
        # play the solutions
        for x in row1_solution:
            pick = x
            play(game, pick)
            print(game)
        # row 2's resolution
        row2_solution = []
        location = 0
        for x in game:
            for y in x:
                location += 1
                if y == 1:
                    if location < 11:
                        row2_solution.append(location + 5)
                        final_solution.append(location + 5) 
        print("")
        print("The order you should click the lights is: ", row2_solution)
        # play the solutions
        for x in row2_solution:
            pick = x
            play(game, pick)
            print(game)
        # row 3's resolution
        row3_solution = []
        location = 0
        for x in game:
            for y in x:
                location += 1
                if y == 1:
                    if location < 16:
                        row3_solution.append(location + 5)
                        final_solution.append(location + 5) 
        print("")
        print("The order you should click the lights is: ", row3_solution)
        # play the solutions
        for x in row3_solution:
            pick = x
            play(game, pick)
            print(game)
        # row 4's resolution
        row4_solution = []
        location = 0
        for x in game:
            for y in x:
                location += 1
                if y == 1:
                    if location < 21:
                        row4_solution.append(location + 5)
                        final_solution.append(location + 5) 
        print("")
        print("The order you should click the lights is: ", row4_solution)
        # play the solutions
        for x in row4_solution:
            pick = x
            play(game, pick)
            print(game)
        # row 5's resolution
        row5_solution = []
        location = 0
        stop = 0
        for x in game:
            for y in x:
                location += 1
                if y == 1:
                    if location < 26:
                        if location == 21:
                            row5_solution.append(4)
                            final_solution.append(4) 
                            row5_solution.append(5)
                            final_solution.append(5) 
                            stop = 1 
                            print("The order you should click the lights is: ", row5_solution)
                            # play the solutions
                            for x in row5_solution:
                                pick = x
                                play(game, pick)
                                print(game)
                        if location == 22 and stop != 1:
                                row5_solution.append(2)
                                final_solution.append(2) 
                                row5_solution.append(5)
                                final_solution.append(5) 
                                stop = 1
                                print("The order you should click the lights is: ", row5_solution)
                                # play the solutions
                                for x in row5_solution:
                                    pick = x
                                    play(game, pick)
                                    print(game)
                        if location == 23 and stop != 1:
                            row5_solution.append(4)
                            final_solution.append(4) 
                            stop = 1
                            print("The order you should click the lights is: ", row5_solution)
                            # play the solutions
                            for x in row5_solution:
                                    pick = x
                                    play(game, pick)
                                    print(game)
    # closes the while loop here in case the game is won
    if impossible != 100:
        print("")
        print("Congratulations, the game is resolved!")
        print("Here are your options:")
        print("")
        print("1.) Final Solution (in steps taken)")
        print("2.) Final Solution (in coordinates)")
        print("3.) Take me back to the Main Menu")
        print("")
        final_coordinates = []
        for x in final_solution:
            pick = x
            coordinates = translate(pick)
            final_coordinates.append(coordinates)

        # print final answer
        def final_answer():
            while True:
                try:
                    question = int(input("Your choice: "))
                    break
                except:
                    print("")
                    print("Invalid option. Please try again.")
                    print("")
                    print("1.) Final Solution (in steps taken)")
                    print("2.) Final Solution (in coordinates)")
                    print("3.) Take me back to the Main Menu")
                    print("")
                
            if question == 1:
                print(final_solution)
            if question == 2:
                print(final_coordinates)
            if question == 3:
                from main import main
                main()      
            else:
                print("")
                print("Invalid option. Please try again.")
                print("")
                print("1.) Final Solution (in steps taken)")
                print("2.) Final Solution (in coordinates)")
                print("3.) Take me back to the Main Menu")
                print("")
                final_answer()
        final_answer()

    else:
        print("")
        print("This is not a possible game to solve!")
