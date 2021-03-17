import numpy as np

"""
row1 = list(map(int, input("row #1: ").split()))
row2 = list(map(int, input("row #2: ").split()))
rows = [row1,row2]
game = np.array(rows)
print(game)

solution = []
location = 0
for x in game:
    for y in x:
        location += 1
        if y == 1:
            if location < 6:
                solution.append(location + 5)
print(solution)
"""
"""
row1 = list(map(int, input("row #1: ").split()))
row2 = list(map(int, input("row #2: ").split()))
row3 = list(map(int, input("row #3: ").split()))
rows = [row1,row2, row3]
game = np.array(rows)
print(game)

print("")

pick = int(input("pick a number: "))
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





print(game[finalpick])




"""

x = 0
for x in range(10):
    x = x + 1
    if x == 1:
        print("1")
        break
    if x == 2 and x != 1:
        print("2")
        break
    if x == 3 and x != 2 and x != 1:
        print("3")
        break
    continue
print("hi")


