import numpy as np

print("")

print("1 - First open the following website on your browser of choice:") 
print("https://www.geogebra.org/m/JexnDJpt#material/RmRUx8Yd")
print("")
print("We will be solving a 5 by 5 lightsout puzzle")
print("2 - First click on the button 'restart' and than on 'random'.")
print("3 - Next, please enter the inputs of each row")
print("4 - 1 is equal to a light on, and a zero is equal to a lights out")
print("5 - There should be 5 numbers per row.")
print("6 - Please enter each of the inputs of the random lights out game and separate them by a space")

row1 = list(map(int, input("row #1: ").split()))
row2 = list(map(int, input("row #2: ").split()))
row3 = list(map(int, input("row #3: ").split()))
row4 = list(map(int, input("row #4: ").split()))
row5 = list(map(int, input("row #5: ").split()))

print("")

rows = [row1,row2,row3,row4,row5]
game = np.array(rows)
print(game)
print("hello")
