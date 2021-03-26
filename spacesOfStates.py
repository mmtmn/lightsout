# made by Thiago M Nóbrega
# to run this project: python main.py

import sys
sys.setrecursionlimit(1500)

import numpy as np
from game3x3 import play
from translator3x3 import translate
from random import randrange

print("")
print("1 - First open the following website on your browser of choice:") 
print("https://www.geogebra.org/m/JexnDJpt#material/RmRUx8Yd")
print("")
print("We will be solving a 3 by 3 lights out puzzle")
print("2 - First click on the button 'restart' and than on 'random'.")
print("3 - Next, please enter the inputs of each row")
print("4 - 1 is equal to a light on, and a zero is equal to a light off")
print("5 - There should be 5 numbers per row.")
print("6 - Please enter each of the inputs of the lights out game and separate them by a space, when finished, please press enter...")

def SpacesOfStatesResolution():
    """ Main function of the software
    """
    # collecting input for inicial space's position
    # collecting row1's inputs
    row1 = list(map(int, input("row #1: ").split()))
    # making sure row have 5 digits
    while len(row1) != 3:
        row1.clear()
        row1 = list(map(int, input("row #1: ").split()))
    # making sure digits are either zero or one
    if len(row1) == 3:
        for x in row1:
            if x != 1 and x != 0:
                row1.clear()
                row1 = list(map(int, input("row #1: ").split()))
    # collecting row2's inputs
    row2 = list(map(int, input("row #2: ").split()))
    while len(row2) != 3:
        row2.clear()
        row2 = list(map(int, input("row #2: ").split()))
    if len(row2) == 3:
        for x in row2:
            if x != 1 and x != 0:
                row2.clear()
                row2 = list(map(int, input("row #2: ").split()))
    # collecting row3's inputs
    row3 = list(map(int, input("row #3: ").split()))
    while len(row3) != 3:
        row3.clear()
        row3 = list(map(int, input("row #3: ").split()))
    if len(row3) == 3:
        for x in row3:
            if x != 1 and x != 0:
                row3.clear()
                row3 = list(map(int, input("row #3: ").split()))
   
    # all the data was collected for the inicial spacial state
    rows = [row1,row2,row3]
    # turning the rows into a 5x5 numpy array
    game = np.array(rows)
    game_states = []
    count = 0
    while count in range(10000):
        count +=1
        print(count)
        pick = randrange(10)
        game_states.append(pick)
        play(game,pick)
        print(game)
        if np.count_nonzero(game) == False:
            print("a solution was found")
            print(game_states)
            break
    print("finish")



    #print(game)
    #if game not in sets:
    #    sets.append(game)
    #pick = 1
   

    #while np.count_nonzero(game):
        #while pick >= 9:
    #play(game,pick)
    #print(game)
            #pick += 1
    #print("Congratulations you solved the game!")


    # list that carries over 
    # all operations for final response
    #final_solution = []
    #gamesets = []
    #print(game)
    #gamesets.append(game)
    #print(gamesets)
    #pick = [0,0]
    #play(pick,game)
    #print(game)
    
    """
    #while np.count_nonzero(game):
    while pick == 9:
        pick += 1
        play(game,pick)
        print(game)

        #gamesets.append(game)
        #print(gamesets)
        
        #1
        for x in game:
            for y in x:
                play(game, pick)
                print(game)
                if game not in gamesets:
                    gamesets.append(game)
                else:
                    play(game,pick)

       
        #2
        for x in game:
            for y in x:
                pick = 2
                play(game, pick)
                print(game)
                if game not in gamesets:
                    gamesets.append(game)
                else:
                    play(game,pick)

        for x in game:
            for y in x:
                pick = 3
                play(game, pick)
                print(game)
                if game not in gamesets:
                    gamesets.append(game)
                else:
                    play(game,pick)

        for x in game:
            for y in x:
                pick = 4
                play(game, pick)
                print(game)
                if game not in gamesets:
                    gamesets.append(game)
                else:
                    play(game,pick)

        for x in game:
            for y in x:
                pick = 5
                play(game, pick)
                print(game)
                if game not in gamesets:
                    gamesets.append(game)
                else:
                    play(game,pick)

        for x in game:
            for y in x:
                pick = 6
                play(game, pick)
                print(game)
                if game not in gamesets:
                    gamesets.append(game)
                else:
                    play(game,pick)

        for x in game:
            for y in x:
                pick = 7
                play(game, pick)
                print(game)
                if game not in gamesets:
                    gamesets.append(game)
                else:
                    play(game,pick)

        for x in game:
            for y in x:
                pick = 8
                play(game, pick)
                print(game)
                if game not in gamesets:
                    gamesets.append(game)
                else:
                    play(game,pick)

        for x in game:
            for y in x:
                pick = 9
                play(game, pick)
                print(game)
                if game not in gamesets:
                    gamesets.append(game)
                else:
                    play(game,pick)
                    
    print(gamesets)


        

    
   
            # roll back to game before state
            #clear random var
    
    # variable that makes sure the game is not impossible
    impossible = 0
    # important while loop that ends when game is resolved
    while np.count_nonzero(game) and impossible != 10:
        impossible += 1
        print(impossible)
        
        # list to keep track of row's solutions and game's next steps
        row1_solution = []
        # keeps track of which spece of state is being validated
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
    if impossible != 10:
        print("")
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
        
    else:
        print("")
        print("This is not a possible game to solve!")
    
    """