# made by Thiago M Nóbrega
# to run this project: python main.py


def translate(pick):
    """
    receives numerical state of space, outputs finalpick as a coordenate
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
        finalpick = 1,0 
    elif pick == 5:
        finalpick = 1,1 
    elif pick == 6:
        finalpick = 1,2 
    elif pick == 7:
        finalpick = 2,0 
    elif pick == 8:
        finalpick = 2,1 
    elif pick == 9:
        finalpick = 2,2 