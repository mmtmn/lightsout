# made by Thiago M Nóbrega
# to run this project: python main.py

import numpy as np
from game3x3 import play
from translator3x3 import translate

import os


print("")
print("We will be solving a 3 by 3 lights out puzzle")
print("")
print("Instructions:")
print("")
print("1.) First open the following website on your browser of choice:") 
print("https://www.geogebra.org/m/JexnDJpt#material/uMG8BYsH")
print("2.) Now, click on the button 'restart' and than on 'random'.")
print("3.) Next, please enter the inputs of each row")
print("4.) The inputs should be either 1 or 0. The number 1 is equal to a light on, and a zero is equal to a light off")
print("5.) There should be 3 numbers per row.")
print("6.) Please enter each of the inputs of the lights out game, by row, separating each value by a space, when finished, please press enter...")

def StateSpace():
    """ This function solves the game by using states of spaces
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
                print("exemple: 1 1 1")
                print("exemple: 0 0 0")
                print("exemple: 1 0 1")
                print("")        

        
        while len(row1) != 3:
            print("")
            print("Invalid option. Please try again.")
            print("exemple: 1 1 1")
            print("exemple: 0 0 0")
            print("exemple: 1 0 1")
            print("")   
            row1.clear()
            row1 = list(map(int, input("row #1: ").split()))
        if len(row1) == 3:
            for x in row1:
                if x != 1 and x != 0:
                    print("")
                    print("Invalid option. Please try again.")
                    print("exemple: 1 1 1")
                    print("exemple: 0 0 0")
                    print("exemple: 1 0 1")
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
                print("exemple: 1 1 1")
                print("exemple: 0 0 0")
                print("exemple: 1 0 1")
                print("")        

        
        while len(row2) != 3:
            print("")
            print("Invalid option. Please try again.")
            print("exemple: 1 1 1")
            print("exemple: 0 0 0")
            print("exemple: 1 0 1")
            print("")   
            row2.clear()
            row2 = list(map(int, input("row #2: ").split()))
        if len(row2) == 3:
            for x in row2:
                if x != 1 and x != 0:
                    print("")
                    print("Invalid option. Please try again.")
                    print("exemple: 1 1 1")
                    print("exemple: 0 0 0")
                    print("exemple: 1 0 1")
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
                print("exemple: 1 1 1")
                print("exemple: 0 0 0")
                print("exemple: 1 0 1")
                print("")        

        
        while len(row3) != 3:
            print("")
            print("Invalid option. Please try again.")
            print("exemple: 1 1 1")
            print("exemple: 0 0 0")
            print("exemple: 1 0 1")
            print("") 
            row3.clear()
            row3 = list(map(int, input("row #3: ").split()))
        if len(row3) == 3:
            for x in row3:
                if x != 1 and x != 0:
                    print("")
                    print("Invalid option. Please try again.")
                    print("exemple: 1 1 1")
                    print("exemple: 0 0 0")
                    print("exemple: 1 0 1")
                    print("") 
                    row3.clear()
                    row3 = list(map(int, input("row #3: ").split()))
        return row3


    # all the data was collected for the inicial spacial state
    rows = [row1_fun(),row2_fun(),row3_fun()]
    # turning the rows into a 5x5 numpy array
    game = np.array(rows)
    sets = []

    # overkill of lists
    lists = [[] for i in range(10000)]
    lists1 = [[] for i in range(10000)]
    # --- copies and appends np array ---
    c = np.copy(game)
    # turns numpy array into string so I can compare them  
    c1 = np.array2string(c)
    lists[0].append(c1)
    lists1[0].append(c)
    sets_values = []
    sets.append(c1)
    sets_values.append(c)
    control = 0
    
    # --- state space core logic ---
    picks = []
    while np.count_nonzero(game):
        game = lists1[0][control]
        pick = 1
        picks.append(pick)
        for pick in range(9):
            pick += 1
            picks.append(pick)
            play(game,pick)
            d = np.copy(game)
            print("")
            print(d)
            d1 = np.array2string(d)
            
            if d1 not in sets:
                sets.append(d1)
                sets_values.append(d)
                lists[0].append(d1)
                lists1[0].append(d)
            else:
                pass
            del d, d1
        control += 1
    print("Congratulations, the game is resolved!")
    print("Amount of plays made until the game was beaten: ", len(picks))
    print("")
    print("1.) Final Solution (in steps taken)")
    print("2.) Final Solution (in coordinates)")
    print("3.) Take me back to the Main Menu")
    print("")
    
    # translate picks to coordinates
    final_coordinates = []
    for x in picks:
        pick = x
        coordinates = translate(pick)
        final_coordinates.append(coordinates)

    # print final answer
    def final_answer():
        while True:
            try:
                question = int(input('Your choice: '))
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
            os.system('cls||clear')
            print(picks)
        if question == 2:
            os.system('cls||clear')
            print(final_coordinates)
        if question == 3:
            os.system('cls||clear')
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
