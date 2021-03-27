# made by Thiago M Nóbrega
# to run this project: python main.py

obj = [[] for i in range(10000)]
print(obj)

#x = 0
#for x in range(100):
#    x += 1
#    obj[x].append(x)
#    obj[x-1].append(x-1)
#    print(obj)

"""
    x = 0
    pick = 1
    side_list = []
    for x in range(10):
        x += 1
        play(game,pick)
        # --- copy&&append
        d = np.copy(game)
        side_list.append(d)
        d1 = np.copy[side_list[x]]
        d2 = np.array2string(d1)

        sets.append(d)
        # sets game to inicial game
        game = np.array(c)
        pick += 1
"""

"""
from random import randrange

list = []
for x in range(10):
    #v = randrange(10)
    v = 1
    print("working")
    if v not in list:
        list.append(v)
        print(v)
print(list)
    

def inicialInputs():
    row1 = list(map(int, input("row #1: ").split()))
    row2 = list(map(int, input("row #2: ").split()))

    if len(row1) != 5:
        while len(row1) != 5:
            row1 = list(map(int, input("row #1: ").split()))
            for x in row1:
                if x != 0 and x != 1:
                    row1 = list(map(int, input("row #1: ").split()))
    
    if len(row2) != 5:
        while len(row2) != 5:
            row2 = list(map(int, input("row #2: ").split()))
            for x in row2:
                if x != 0 and x != 1:
                    row2 = list(map(int, input("row #2: ").split()))
    return row1,row2
inicialInputs()
a = inicialInputs()
print(a)


print("nice!")
"""
"""
import random

n = random.randint(0,5)
print(n,n,n,n,n)
"""

"""
from translator import translate

list = [25, 1, 2]
list2 = []
for x in list:
    pick = x
    coordinates = translate(pick)
    list2.append(coordinates)
print(list2)
"""


"""
import numpy as np
from game import play

def lightsOutResolution():
    row1 = list(map(int, input("row #1: ").split()))
    row2 = list(map(int, input("row #2: ").split()))
    row3 = list(map(int, input("row #3: ").split()))
    row4 = list(map(int, input("row #4: ").split()))
    row5 = list(map(int, input("row #5: ").split()))
    rows = [row1,row2,row3,row4,row5]
    #inicial_game = np.array(rows)
    game = np.array(rows)
    print(game)
    #while np.count_nonzero(game):
    row1_solution = []
    location = 0
    for x in game:
        for y in x:
            location += 1
            if y == 1:
                if location < 6:
                    row1_solution.append(location + 5)
    print("")
    print("The order you should click the lights is: ", row1_solution)

    for x in row1_solution:
        pick = x
        play(game, pick)
        print(game)
    #print(pick)

lightsOutResolution()
"""