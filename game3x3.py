# made by Thiago M Nóbrega
# to run this project: python main.py

def play(game, pick):
    """ This is the set of all possible actions,
        everytime a play is made this function is called
        the new state of the game is returned
    """

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
        
        if game[1,2] != 0:
            game[1,2] = 0
        elif game[1,2] != 1:
            game[1,2] = 1

    # btn4
    if pick == 4:
        if game[1,0] != 0:
            game[1,0] = 0
        elif game[1,0] != 1:
            game[1,0] = 1
        
        if game[1,1] != 0:
            game[1,1] = 0
        elif game[1,1] != 1:
            game[1,1] = 1
        
        if game[0,0] != 0:
            game[0,0] = 0
        elif game[0,0] != 1:
            game[0,0] = 1
        
        if game[2,0] != 0:
            game[2,0] = 0
        elif game[2,0] != 1:
            game[2,0] = 1

    # btn4
    if pick == 5:
        if game[1,1] != 0:
            game[1,1] = 0
        elif game[1,1] != 1:
            game[1,1] = 1
        
        if game[1,2] != 0:
            game[1,2] = 0
        elif game[1,2] != 1:
            game[1,2] = 1
        
        if game[0,1] != 0:
            game[0,1] = 0
        elif game[0,1] != 1:
            game[0,1] = 1
        
        if game[2,1] != 0:
            game[2,1] = 0
        elif game[2,1] != 1:
            game[2,1] = 1

        if game[1,0] != 0:
            game[1,0] = 0
        elif game[1,0] != 1:
            game[1,0] = 1
    
    if pick == 6:
        if game[1,2] != 0:
            game[1,2] = 0
        elif game[1,2] != 1:
            game[1,2] = 1
        
        if game[1,1] != 0:
            game[1,1] = 0
        elif game[1,1] != 1:
            game[1,1] = 1
        
        if game[0,2] != 0:
            game[0,2] = 0
        elif game[0,2] != 1:
            game[0,2] = 1
        
        if game[2,2] != 0:
            game[2,2] = 0
        elif game[2,2] != 1:
            game[2,2] = 1
    
    if pick == 7:
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
    
    if pick == 8:
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
        
        if game[2,2] != 0:
            game[2,2] = 0
        elif game[2,2] != 1:
            game[2,2] = 1
    
    if pick == 9:
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
    return(game)