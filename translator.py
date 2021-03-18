# made by Thiago M Nóbrega

def translate(pick):
    """
    receives pick, outputs finalpick
    """
    #pick = int(input("pick a number: "))
    x1 = 0
    y0 = 0
    if pick == 1:
        finalpick = 0,0
    elif pick == 2:
        finalpick = 0,1
    elif pick == 3:
        finalpick = 0,2 
    elif pick == 4:
        finalpick = 0,3 
    elif pick == 5:
        finalpick = 0,4 
    elif pick == 6:
        finalpick = 1,0 
    elif pick == 7:
        finalpick = 1,1 
    elif pick == 8:
        finalpick = 1,2 
    elif pick == 9:
        finalpick = 1,3 
    elif pick == 10:
        finalpick = 1,4
    elif pick == 11:
        finalpick = 2,0 
    elif pick == 12:
        finalpick = 2,1 
    elif pick == 13:
        finalpick = 2,2 
    elif pick == 14:
        finalpick = 2,3 
    elif pick == 15:
        finalpick = 2,4
    elif pick == 16:
        finalpick = 3,0
    elif pick == 17:
        finalpick = 3,1
    elif pick == 18:
        finalpick = 3,2
    elif pick == 19:
        finalpick = 3,3
    elif pick == 20:
        finalpick = 3,4
    elif pick == 21:
        finalpick = 4,0
    elif pick == 22:
        finalpick = 4,1
    elif pick == 23:
        finalpick = 4,2
    elif pick == 24:
        finalpick = 4,3
    elif pick == 25:
        finalpick = 4,4
    
    return finalpick