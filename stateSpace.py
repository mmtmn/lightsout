# made by Thiago M Nóbrega
# to run this project: python main.py

import sys
sys.setrecursionlimit(1500)

import numpy as np
from game3x3 import play
from translator3x3 import translate

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

def StateSpace():
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
            print(picks)
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
