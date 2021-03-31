# made by Thiago M Nóbrega
# to run this project: python main.py

import numpy as np
from game5x5 import play
from translator5x5 import translate

print("")
print("We will be solving a 5 by 5 lights out puzzle")
print("")
print("Instructions:")
print("")
print("1.) First open the following website on your browser of choice:") 
print("https://www.geogebra.org/m/JexnDJpt#material/RmRUx8Yd")
print("2.) Now, click on the button 'restart' and than on 'random'.")
print("3.) Next, please enter the inputs of each row")
print("4.) The inputs should be either 1 or 0. The number 1 is equal to a light on, and a zero is equal to a light off")
print("5.) There should be 5 numbers per row.")
print("6.) Please enter each of the inputs of the lights out game, by row, separating each value by a space, when finished, please press enter...")

def HeuristicsResolution():
    """ This function solves the game by using heuristics
        returns the solution while getting inputs
    """
    # collecting input for inicial space's position

    # collecting row1's inputs
    def row1_fun():
        while True:
            try:
                row1 = list(map(int, input("row #1: ").split()))
                break
            except:
                print("")
                print("Invalid option. Please try again.")
                print("exemple: 1 1 1 1 1")
                print("exemple: 0 0 0 0 0")
                print("exemple: 1 0 1 0 1")
                print("")        

        
        while len(row1) != 5:
            print("")
            print("Invalid option. Please try again.")
            print("exemple: 1 1 1 1 1")
            print("exemple: 0 0 0 0 0")
            print("exemple: 1 0 1 0 1")
            print("")   
            row1.clear()
            row1 = list(map(int, input("row #1: ").split()))
        if len(row1) == 5:
            for x in row1:
                if x != 1 and x != 0:
                    print("")
                    print("Invalid option. Please try again.")
                    print("exemple: 1 1 1 1 1")
                    print("exemple: 0 0 0 0 0")
                    print("exemple: 1 0 1 0 1")
                    print("")   
                    row1.clear()
                    row1 = list(map(int, input("row #1: ").split()))
        return row1
    
    def row2_fun():
        while True:
            try:
                row2 = list(map(int, input("row #2: ").split()))
                break
            except:
                print("")
                print("Invalid option. Please try again.")
                print("exemple: 1 1 1 1 1")
                print("exemple: 0 0 0 0 0")
                print("exemple: 1 0 1 0 1")
                print("")        

        
        while len(row2) != 5:
            print("")
            print("Invalid option. Please try again.")
            print("exemple: 1 1 1 1 1")
            print("exemple: 0 0 0 0 0")
            print("exemple: 1 0 1 0 1")
            print("")   
            row2.clear()
            row2 = list(map(int, input("row #2: ").split()))
        if len(row2) == 5:
            for x in row2:
                if x != 1 and x != 0:
                    print("")
                    print("Invalid option. Please try again.")
                    print("exemple: 1 1 1 1 1")
                    print("exemple: 0 0 0 0 0")
                    print("exemple: 1 0 1 0 1")
                    print("") 
                    row2.clear()
                    row2 = list(map(int, input("row #2: ").split()))
        return row2
    
    def row3_fun():
        while True:
            try:
                row3 = list(map(int, input("row #3: ").split()))
                break
            except:
                print("")
                print("Invalid option. Please try again.")
                print("exemple: 1 1 1 1 1")
                print("exemple: 0 0 0 0 0")
                print("exemple: 1 0 1 0 1")
                print("")        

        
        while len(row3) != 5:
            print("")
            print("Invalid option. Please try again.")
            print("exemple: 1 1 1 1 1")
            print("exemple: 0 0 0 0 0")
            print("exemple: 1 0 1 0 1")
            print("") 
            row3.clear()
            row3 = list(map(int, input("row #3: ").split()))
        if len(row3) == 5:
            for x in row3:
                if x != 1 and x != 0:
                    print("")
                    print("Invalid option. Please try again.")
                    print("exemple: 1 1 1 1 1")
                    print("exemple: 0 0 0 0 0")
                    print("exemple: 1 0 1 0 1")
                    print("") 
                    row3.clear()
                    row3 = list(map(int, input("row #3: ").split()))
        return row3
    
    def row4_fun():
        while True:
            try:
                row4 = list(map(int, input("row #4: ").split()))
                break
            except:
                print("")
                print("Invalid option. Please try again.")
                print("exemple: 1 1 1 1 1")
                print("exemple: 0 0 0 0 0")
                print("exemple: 1 0 1 0 1")
                print("")        

        
        while len(row4) != 5:
            print("")
            print("Invalid option. Please try again.")
            print("exemple: 1 1 1 1 1")
            print("exemple: 0 0 0 0 0")
            print("exemple: 1 0 1 0 1")
            print("") 
            row4.clear()
            row4 = list(map(int, input("row #4: ").split()))
        if len(row4) == 5:
            for x in row4:
                if x != 1 and x != 0:
                    print("")
                    print("Invalid option. Please try again.")
                    print("exemple: 1 1 1 1 1")
                    print("exemple: 0 0 0 0 0")
                    print("exemple: 1 0 1 0 1")
                    print("") 
                    row4.clear()
                    row4 = list(map(int, input("row #4: ").split()))
        return row4
    
    def row5_fun():
        while True:
            try:
                row5 = list(map(int, input("row #5: ").split()))
                break
            except:
                print("")
                print("Invalid option. Please try again.")
                print("exemple: 1 1 1 1 1")
                print("exemple: 0 0 0 0 0")
                print("exemple: 1 0 1 0 1")
                print("")        

        
        while len(row5) != 5:
            print("")
            print("Invalid option. Please try again.")
            print("exemple: 1 1 1 1 1")
            print("exemple: 0 0 0 0 0")
            print("exemple: 1 0 1 0 1")
            print("") 
            row5.clear()
            row5 = list(map(int, input("row #5: ").split()))
        if len(row5) == 5:
            for x in row5:
                if x != 1 and x != 0:
                    print("")
                    print("Invalid option. Please try again.")
                    print("exemple: 1 1 1 1 1")
                    print("exemple: 0 0 0 0 0")
                    print("exemple: 1 0 1 0 1")
                    print("") 
                    row5.clear()
                    row5 = list(map(int, input("row #5: ").split()))
        return row5

    # all the data was collected for the inicial spacial state

    rows = [row1_fun(),row2_fun(),row3_fun(),row4_fun(),row5_fun()]
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
