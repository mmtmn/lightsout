# made by Thiago M Nóbrega
# to run this project: python main.py

import numpy as np
from game3x3 import play
from translator3x3 import translate
from random import randrange

print("")
print("We will be solving a 5 by 5 lights out puzzle")
print("")
print("Instructions:")
print("")
print("1.) First open the following website on your browser of choice:") 
print("https://www.geogebra.org/m/JexnDJpt#material/uMG8BYsH")
print("2.) Now, click on the button 'restart' and than on 'random'.")
print("3.) Next, please enter the inputs of each row")
print("4.) The inputs should be either 1 or 0. The number 1 is equal to a light on, and a zero is equal to a light off")
print("5.) There should be 5 numbers per row.")
print("6.) Please enter each of the inputs of the lights out game, by row, separating each value by a space, when finished, please press enter...")

def BruteForce():
    """ This function solves the game by brute forcing randomly 
        returns the solution while getting inputs
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
    while count in range(100000):
        count +=1
        print(count)
        pick = randrange(10)
        game_states.append(pick)
        play(game,pick)
        print(game)
        if np.count_nonzero(game) == False:
            print("")
            print("Congratulations, the game is resolved!")
            print("")
            print("1.) Final Solution (in steps taken)")
            print("2.) Final Solution (in coordinates)")
            print("3.) Take me back to the Main Menu")
            print("")

            # translate picks (or steps) to coordinates
            final_coordinates = []
            for x in game_states:
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
                    print(game_states)
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
