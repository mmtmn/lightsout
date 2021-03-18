# made by Thiago M Nóbrega

import numpy as np
from game import play
from translator import translate

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

def lightsOutResolution():
    row1 = list(map(int, input("row #1: ").split()))
    row2 = list(map(int, input("row #2: ").split()))
    row3 = list(map(int, input("row #3: ").split()))
    row4 = list(map(int, input("row #4: ").split()))
    row5 = list(map(int, input("row #5: ").split()))
    rows = [row1,row2,row3,row4,row5]
    game = np.array(rows)
    final_solution = []
    print(game)
    while np.count_nonzero(game):
        row1_solution = []
        location = 0
        for x in game:
            for y in x:
                location += 1
                if y == 1:
                    if location < 6:
                        row1_solution.append(location + 5)
                        final_solution.append(location + 5) 
        print("")
        print("The order you should click the lights is: ", row1_solution)
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
        gameover = 0
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
    # closing while loop in case game is won
    print("Congratulations, the game is resolved!")
    final_coordinates = []
    for x in final_solution:
        pick = x
        coordinates = translate(pick)
        final_coordinates.append(coordinates)
    print("To win this game, you must press the following buttons in this specific order:", final_solution)
    print("To be even more clear, you must press the buttons on the following coordinates: ")
    for x in final_coordinates:
        print(x)
lightsOutResolution()
