# made by Thiago M Nóbrega
# to run this project: python main.py


import numpy as np

def play(game, pick):
    #row1 = list(map(int, input("row #1: ").split()))
    #row2 = list(map(int, input("row #2: ").split()))
    #row3 = list(map(int, input("row #3: ").split()))
    #row4 = list(map(int, input("row #4: ").split()))
    #row5 = list(map(int, input("row #5: ").split()))
    #rows = [row1,row2,row3,row4,row5]
    #game = np.array(rows)
    #print(game)

    #pick = int(input("pick: "))

    # btn1
    if pick == 1:
        if game[0,0] != 0:
            game[0,0] = 0
        elif game[0,0] != 1:
            game[0,0] = 1
        
        if game[1,0] != 0:
            game[1,0] = 0
        elif game[1,0] != 1:
            game[1,0] = 1
        
        if game[0,1] != 0:
            game[0,1] = 0
        elif game[0,1] != 1:
            game[0,1] = 1

    # btn2
    if pick == 2:
        if game[0,1] != 0:
            game[0,1] = 0
        elif game[0,1] != 1:
            game[0,1] = 1
        
        if game[0,0] != 0:
            game[0,0] = 0
        elif game[0,0] != 1:
            game[0,0] = 1
        
        if game[0,2] != 0:
            game[0,2] = 0
        elif game[0,2] != 1:
            game[0,2] = 1
        
        if game[1,1] != 0:
            game[1,1] = 0
        elif game[1,1] != 1:
            game[1,1] = 1

    # btn3
    if pick == 3:
        if game[0,2] != 0:
            game[0,2] = 0
        elif game[0,2] != 1:
            game[0,2] = 1
        
        if game[0,1] != 0:
            game[0,1] = 0
        elif game[0,1] != 1:
            game[0,1] = 1
        
        if game[0,3] != 0:
            game[0,3] = 0
        elif game[0,3] != 1:
            game[0,3] = 1
        
        if game[1,2] != 0:
            game[1,2] = 0
        elif game[1,2] != 1:
            game[1,2] = 1

    # btn4
    if pick == 4:
        if game[0,3] != 0:
            game[0,3] = 0
        elif game[0,3] != 1:
            game[0,3] = 1
        
        if game[0,2] != 0:
            game[0,2] = 0
        elif game[0,2] != 1:
            game[0,2] = 1
        
        if game[0,4] != 0:
            game[0,4] = 0
        elif game[0,4] != 1:
            game[0,4] = 1
        
        if game[1,3] != 0:
            game[1,3] = 0
        elif game[1,3] != 1:
            game[1,3] = 1

    # btn5
    if pick == 5:
        if game[0,4] != 0:
            game[0,4] = 0
        elif game[0,4] != 1:
            game[0,4] = 1
        
        if game[0,3] != 0:
            game[0,3] = 0
        elif game[0,3] != 1:
            game[0,3] = 1
        
        if game[1,4] != 0:
            game[1,4] = 0
        elif game[1,4] != 1:
            game[1,4] = 1

    # btn6
    if pick == 6:
        if game[1,0] != 0:
            game[1,0] = 0
        elif game[1,0] != 1:
            game[1,0] = 1
        
        if game[0,0] != 0:
            game[0,0] = 0
        elif game[0,0] != 1:
            game[0,0] = 1
        
        if game[1,1] != 0:
            game[1,1] = 0
        elif game[1,1] != 1:
            game[1,1] = 1

        if game[2,0] != 0:
            game[2,0] = 0
        elif game[2,0] != 1:
            game[2,0] = 1

    # btn7
    if pick == 7:
        if game[1,1] != 0:
            game[1,1] = 0
        elif game[1,1] != 1:
            game[1,1] = 1
        
        if game[0,1] != 0:
            game[0,1] = 0
        elif game[0,1] != 1:
            game[0,1] = 1
        
        if game[1,0] != 0:
            game[1,0] = 0
        elif game[1,0] != 1:
            game[1,0] = 1

        if game[1,2] != 0:
            game[1,2] = 0
        elif game[1,2] != 1:
            game[1,2] = 1

        if game[2,1] != 0:
            game[2,1] = 0
        elif game[2,1] != 1:
            game[2,1] = 1

    # btn8
    if pick == 8:
        if game[1,2] != 0:
            game[1,2] = 0
        elif game[1,2] != 1:
            game[1,2] = 1
        
        if game[0,2] != 0:
            game[0,2] = 0
        elif game[0,2] != 1:
            game[0,2] = 1
        
        if game[1,1] != 0:
            game[1,1] = 0
        elif game[1,1] != 1:
            game[1,1] = 1

        if game[1,3] != 0:
            game[1,3] = 0
        elif game[1,3] != 1:
            game[1,3] = 1

        if game[2,2] != 0:
            game[2,2] = 0
        elif game[2,2] != 1:
            game[2,2] = 1

    # btn9
    if pick == 9:
        if game[1,3] != 0:
            game[1,3] = 0
        elif game[1,3] != 1:
            game[1,3] = 1
        
        if game[0,3] != 0:
            game[0,3] = 0
        elif game[0,3] != 1:
            game[0,3] = 1
        
        if game[1,2] != 0:
            game[1,2] = 0
        elif game[1,2] != 1:
            game[1,2] = 1

        if game[1,4] != 0:
            game[1,4] = 0
        elif game[1,4] != 1:
            game[1,4] = 1

        if game[2,3] != 0:
            game[2,3] = 0
        elif game[2,3] != 1:
            game[2,3] = 1

    # btn10
    if pick == 10:
        if game[1,4] != 0:
            game[1,4] = 0
        elif game[1,4] != 1:
            game[1,4] = 1
        
        if game[0,4] != 0:
            game[0,4] = 0
        elif game[0,4] != 1:
            game[0,4] = 1
        
        if game[1,3] != 0:
            game[1,3] = 0
        elif game[1,3] != 1:
            game[1,3] = 1

        if game[2,4] != 0:
            game[2,4] = 0
        elif game[2,4] != 1:
            game[2,4] = 1

    # btn11
    if pick == 11:
        if game[2,0] != 0:
            game[2,0] = 0
        elif game[2,0] != 1:
            game[2,0] = 1
        
        if game[1,0] != 0:
            game[1,0] = 0
        elif game[1,0] != 1:
            game[1,0] = 1
        
        if game[2,1] != 0:
            game[2,1] = 0
        elif game[2,1] != 1:
            game[2,1] = 1

        if game[3,0] != 0:
            game[3,0] = 0
        elif game[3,0] != 1:
            game[3,0] = 1

    # btn12
    if pick == 12:
        if game[2,1] != 0:
            game[2,1] = 0
        elif game[2,1] != 1:
            game[2,1] = 1
        
        if game[1,1] != 0:
            game[1,1] = 0
        elif game[1,1] != 1:
            game[1,1] = 1
        
        if game[2,0] != 0:
            game[2,0] = 0
        elif game[2,0] != 1:
            game[2,0] = 1

        if game[3,1] != 0:
            game[3,1] = 0
        elif game[3,1] != 1:
            game[3,1] = 1

        if game[2,2] != 0:
            game[2,2] = 0
        elif game[2,2] != 1:
            game[2,2] = 1

    # btn13
    if pick == 13:
        if game[2,2] != 0:
            game[2,2] = 0
        elif game[2,2] != 1:
            game[2,2] = 1
        
        if game[1,2] != 0:
            game[1,2] = 0
        elif game[1,2] != 1:
            game[1,2] = 1
        
        if game[2,1] != 0:
            game[2,1] = 0
        elif game[2,1] != 1:
            game[2,1] = 1

        if game[3,2] != 0:
            game[3,2] = 0
        elif game[3,2] != 1:
            game[3,2] = 1

        if game[2,3] != 0:
            game[2,3] = 0
        elif game[2,3] != 1:
            game[2,3] = 1

    # btn14
    if pick == 14:
        if game[2,3] != 0:
            game[2,3] = 0
        elif game[2,3] != 1:
            game[2,3] = 1
        
        if game[1,3] != 0:
            game[1,3] = 0
        elif game[1,3] != 1:
            game[1,3] = 1
        
        if game[2,2] != 0:
            game[2,2] = 0
        elif game[2,2] != 1:
            game[2,2] = 1

        if game[3,3] != 0:
            game[3,3] = 0
        elif game[3,3] != 1:
            game[3,3] = 1

        if game[2,4] != 0:
            game[2,4] = 0
        elif game[2,4] != 1:
            game[2,4] = 1
        
    # btn15
    if pick == 15:
        if game[2,4] != 0:
            game[2,4] = 0
        elif game[2,4] != 1:
            game[2,4] = 1
        
        if game[1,4] != 0:
            game[1,4] = 0
        elif game[1,4] != 1:
            game[1,4] = 1
        
        if game[2,3] != 0:
            game[2,3] = 0
        elif game[2,3] != 1:
            game[2,3] = 1

        if game[3,4] != 0:
            game[3,4] = 0
        elif game[3,4] != 1:
            game[3,4] = 1

    # btn16
    if pick == 16:
        if game[3,0] != 0:
            game[3,0] = 0
        elif game[3,0] != 1:
            game[3,0] = 1
        
        if game[2,0] != 0:
            game[2,0] = 0
        elif game[2,0] != 1:
            game[2,0] = 1
        
        if game[3,1] != 0:
            game[3,1] = 0
        elif game[3,1] != 1:
            game[3,1] = 1

        if game[4,0] != 0:
            game[4,0] = 0
        elif game[4,0] != 1:
            game[4,0] = 1

    # btn17
    if pick == 17:
        if game[3,1] != 0:
            game[3,1] = 0
        elif game[3,1] != 1:
            game[3,1] = 1
        
        if game[2,1] != 0:
            game[2,1] = 0
        elif game[2,1] != 1:
            game[2,1] = 1
        
        if game[3,2] != 0:
            game[3,2] = 0
        elif game[3,2] != 1:
            game[3,2] = 1

        if game[4,1] != 0:
            game[4,1] = 0
        elif game[4,1] != 1:
            game[4,1] = 1
        
        if game[3,0] != 0:
            game[3,0] = 0
        elif game[3,0] != 1:
            game[3,0] = 1

    # btn18
    if pick == 18:
        if game[3,2] != 0:
            game[3,2] = 0
        elif game[3,2] != 1:
            game[3,2] = 1
        
        if game[2,2] != 0:
            game[2,2] = 0
        elif game[2,2] != 1:
            game[2,2] = 1
        
        if game[3,3] != 0:
            game[3,3] = 0
        elif game[3,3] != 1:
            game[3,3] = 1

        if game[4,2] != 0:
            game[4,2] = 0
        elif game[4,2] != 1:
            game[4,2] = 1
        
        if game[3,1] != 0:
            game[3,1] = 0
        elif game[3,1] != 1:
            game[3,1] = 1

    # btn19
    if pick == 19:
        if game[3,3] != 0:
            game[3,3] = 0
        elif game[3,3] != 1:
            game[3,3] = 1
        
        if game[2,3] != 0:
            game[2,3] = 0
        elif game[2,3] != 1:
            game[2,3] = 1
        
        if game[3,4] != 0:
            game[3,4] = 0
        elif game[3,4] != 1:
            game[3,4] = 1

        if game[4,3] != 0:
            game[4,3] = 0
        elif game[4,3] != 1:
            game[4,3] = 1
        
        if game[3,2] != 0:
            game[3,2] = 0
        elif game[3,2] != 1:
            game[3,2] = 1

    # btn20
    if pick == 20:
        if game[3,4] != 0:
            game[3,4] = 0
        elif game[3,4] != 1:
            game[3,4] = 1
        
        if game[2,4] != 0:
            game[2,4] = 0
        elif game[2,4] != 1:
            game[2,4] = 1

        if game[4,4] != 0:
            game[4,4] = 0
        elif game[4,4] != 1:
            game[4,4] = 1
        
        if game[3,3] != 0:
            game[3,3] = 0
        elif game[3,3] != 1:
            game[3,3] = 1

    # btn21
    if pick == 21:
        if game[4,0] != 0:
            game[4,0] = 0
        elif game[4,0] != 1:
            game[4,0] = 1
        
        if game[3,0] != 0:
            game[3,0] = 0
        elif game[3,0] != 1:
            game[3,0] = 1

        if game[4,1] != 0:
            game[4,1] = 0
        elif game[4,1] != 1:
            game[4,1] = 1

    # btn22
    if pick == 22:
        if game[4,1] != 0:
            game[4,1] = 0
        elif game[4,1] != 1:
            game[4,1] = 1
        
        if game[3,1] != 0:
            game[3,1] = 0
        elif game[3,1] != 1:
            game[3,1] = 1

        if game[4,2] != 0:
            game[4,2] = 0
        elif game[4,2] != 1:
            game[4,2] = 1
        
        if game[4,0] != 0:
            game[4,0] = 0
        elif game[4,0] != 1:
            game[4,0] = 1

    # btn23
    if pick == 23:
        if game[4,2] != 0:
            game[4,2] = 0
        elif game[4,2] != 1:
            game[4,2] = 1
        
        if game[3,2] != 0:
            game[3,2] = 0
        elif game[3,2] != 1:
            game[3,2] = 1

        if game[4,3] != 0:
            game[4,3] = 0
        elif game[4,3] != 1:
            game[4,3] = 1
        
        if game[4,1] != 0:
            game[4,1] = 0
        elif game[4,1] != 1:
            game[4,1] = 1

    # btn24
    if pick == 24:
        if game[4,3] != 0:
            game[4,3] = 0
        elif game[4,3] != 1:
            game[4,3] = 1
        
        if game[3,3] != 0:
            game[3,3] = 0
        elif game[3,3] != 1:
            game[3,3] = 1

        if game[4,4] != 0:
            game[4,4] = 0
        elif game[4,4] != 1:
            game[4,4] = 1
        
        if game[4,2] != 0:
            game[4,2] = 0
        elif game[4,2] != 1:
            game[4,2] = 1

    # btn25
    if pick == 25:
        if game[4,4] != 0:
            game[4,4] = 0
        elif game[4,4] != 1:
            game[4,4] = 1
        
        if game[3,4] != 0:
            game[3,4] = 0
        elif game[3,4] != 1:
            game[3,4] = 1
        
        if game[4,3] != 0:
            game[4,3] = 0
        elif game[4,3] != 1:
            game[4,3] = 1

    #print(game)
    return(game)