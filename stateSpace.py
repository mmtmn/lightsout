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
    lists = [[] for i in range(10000)]
    lists1 = [[] for i in range(10000)]
    # --- copies and appends np array ---
    c = np.copy(game)
    c1 = np.array2string(c)
    lists[0].append(c1)
    lists1[0].append(c)
    sets_values = []
    #print(lists[0])
    sets.append(c1)
    sets_values.append(c)
    control = 0
    
    # --- sets inicial pick for game ---
    
    while np.count_nonzero(game):
        game = lists1[0][control]
        pick = 1
        for pick in range(9):
            pick += 1
            
            #print(pick)
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
    
        
        
    """    
    print("sets_values:")
    # set_values has the np array
    for x in sets_values:
        print("") 
        print(x)

    print("sets:")
    # sets has the np arrays as strings
    for x in sets:
        print("")
        print(x)

    """





""" 
    # 1. play all posibilities
    # def play_all():
    pick = 0
    i = -1
    j = 0
    cycle = 0

    print(lists)

    while i < 1000:
        i += 1
        for x in range(9):
            pick +=1
            play(game,pick)
            print(game)
            hold = np.copy(game)
            hold1 = np.array2string(hold)
            if hold1 not in sets:
                (lists[i+1]).append(hold1)
                print(i)
                # print((lists[i+1]).index())
                sets.append(hold1)
                sets_values.append(hold)
            else:
                pass
            
            #game = np.array(sets_values[i])
            game = np.array(sets_values[i][i])
        #print("----")
   
        
        print(i)


                for x in sets_values:
                    print("")
                    print(x)
                
                for x in sets:
                    print("")
                    print(sets)

    #for x in sets_values:
    #    print("")
    #    print(x)

    #print("list2: ")
    #print(lists[4])

    print("list1")
    for x in lists[1]:
        print("")
        print(x)
    print("list2")
    for x in lists[2]:
        print("")
        print(x)
    # play_all()

    

    

    # 2. add all new states to a new list
    
    # 3. repeat until state is null
















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



    test = []
    game = np.array(c)
    pick = 1
    play(game,pick)
    e = np.copy(game)
    test.append(e)
    e1 = np.copy(test[0])
    e2 = np.array2string(e1)

    
    for x in sets:
        var1 = np.copy(x)
        var2 = np.array2string(var1)
        if (var2==e2):
            
        else:
            pass



    for x in sets:
        print("")
        print(x)

    #d = np.copy(game)
    #se estiver dentro do sets

    if (c == d).all():
        print("working")
    # se não estiver
    else:
        print("wtf")



    # append numpy array
    for x in range(10):
        c = np.copy(game)
        for x in 
        sets.append(c)
        pick += 1
        play(game,pick)
        #print(game)


    for x in sets:
        print("")
        print(x)

        
    



    for pick in range(10):
        play(game,pick)
        print(game)
        pick += 1
        game = inicial_game[0]
  





















    # ------------ nice solution ----------
    #lists = [[] for i in range(10000)]
    # ------------ nice solution ----------

    #lists[1].append(game)



    #loop_counter = 1
    #nine_choices = 0
    #while np.count_nonzero(game):
    #    for loop_counter in range(1000):
    #        loop_counter += 1
    #        print("attempt number:", loop_counter)

    
    #        pickDepth1 = 1
    #        pickDepth2 = 1
    #        pickDepth3 = 1
    #        pickDepeth4 = 1
    #        pickDepeth5 = 1
    #        pickDepeth6 = 1
    #        pickDepeth7 = 1
    #        pickDepeth8 = 1
    #        pickDepeth9 = 1



    a = 1
    b = 1
    L= [0]
    L1 = []
    stop = 0
    #while np.count_nonzero(game):
    while a < 4:
        # 'a' side
        while stop < 10:
            stop += 1
            for a in range(9):
                
                pick = a
                play(game,pick)
                a += 1

                #play
                for x in L:
                    if (x==game).all():    
                        print("repeated")
                        L.append(game)
                    else:
                        L1.append(game)
                
                # a's print
                print("a: ", a)
                print(game)

    print("L: ", L)
    print("L1: ", L1)

            # 'b' side
            for b in range(9):

                pick = b
                play(game,pick)
                b += 1

                #play
                for x in L:
                    if (x==game).all():    
                        print("repeated")
                else:
                    L1.append(game)
                L.append(game)

                # b's print
                print("b: ", b)
                print(game)



                # 'c' side
                for c in range(9):

                    pick = c
                    play(game,pick)
                    c += 1

                    #play
                    if game in L:
                        print("repeated")
                    else:
                        L1.append(game)
                    L.append(game)

                    # c's print
                    print("c: ", c)
                    print(game)
                
                    # 'd' side
                    for d in range(9):

                        pick = d
                        play(game,pick)
                        d += 1

                        #play
                        if game in L:
                            print("repeated")
                        else:
                            L1.append(game)
                        L.append(game)

                        # d's print
                        print("d: ", d)
                        print(game)

                        # 'e' side
                        for e in range(9):

                            pick = e
                            play(game,pick)
                            e += 1

                            #play
                            if game in L:
                                print("repeated")
                            else:
                                L1.append(game)
                            L.append(game)

                            # e's print
                            print("e: ", e)
                            print(game)
                        
                        # 'f' side
                        for f in range(9):

                            pick = f
                            play(game,pick)
                            f += 1

                            #play
                            if game in L:
                                print("repeated")
                            else:
                                L1.append(game)
                            L.append(game)

                            # f's print
                            print("f: ", f)
                            print(game)

                            # 'g' side
                            for g in range(9):

                                pick = g
                                play(game,pick)
                                g += 1

                                #play
                                if game in L:
                                    print("repeated")
                                else:
                                    L1.append(game)
                                L.append(game)

                                # g's print
                                print("g: ", g)
                                print(game)

                                # 'h' side
                                for h in range(9):

                                    pick = h
                                    play(game,pick)
                                    h += 1

                                    #play
                                    if game in L:
                                        print("repeated")
                                    else:
                                        L1.append(game)
                                    L.append(game)

                                    # h's print
                                    print("h: ", h)
                                    print(game)

                                    # 'i' side
                                    for i in range(9):

                                        pick = i
                                        play(game,pick)
                                        i += 1

                                        #play
                                        if game in L:
                                            print("repeated")
                                        else:
                                            L1.append(game)
                                        L.append(game)

                                        # i's print
                                        print("i: ", i)
                                        print(game)
    print("game over")

    # prints
    #print("all:")
    #for x in L:
    #    print(x)
    #    print("")
    
    #print("unique: ")
    #for x in L1:
    #    print(x)
    #    print("")
         
                for pickDepth1 in range(9):
                    pickDepth1 +=1
                    pick = pickDepth1   
                    play(game,pick)
                    #print(game)
                    if game not in lists[1]:
                        lists[1].append(game)
                        print(game)
                    

                    for pickDepth2 in range(9):
                        pickDepth2 +=1
                        pick = pickDepth2   
                        play(game,pick)
                        #print(game)
                        if game not in lists[1]:
                            lists[1].append(game)
                            print(game)
                        
                        
                        for pickDepth3 in range(9):
                            pickDepth3 +=1
                            pick = pickDepth3   
                            play(game,pick)
                            #print(game)
                            if game not in lists[1]:
                                lists[1].append(game)
                                print(game)
                           

                

                





        for nine_choices in range(10):
            nine_choices += 1
            pick = nine_choices
            play(game,pick)

            lists[loop_counter].append(game)
            for x in lists[loop_counter]:
                play(game.pick)
                lists[loop_counter+10].append(game)






    lists[1].append(game)
    print(lists[1])

    #print("")

    pick = 1
    play(game,pick)

    #game_states = []
    #count = 0
    #pick = 1
    #lists = [[] for i in range(10000)]
    #while count in range(3):
       # count +=1
        #print(count)

        #pick += 1
        # creating 10k lists
        
        # memory
    lists[1].append(game)

    # order of picks
    #game_states.append(pick)
    #play(game,pick)
    #print(game)
    #lists[2].append(game)
    print(lists[1])
    #print(lists[2])




        # when game is won
        if np.count_nonzero(game) == False:
            print("")
            print("Congratulations, the game is resolved!")
            final_coordinates = []
            for x in game_states:
                pick = x
                coordinates = translate(pick)
                final_coordinates.append(coordinates)
            print("To win this game, you must press the following buttons in this specific order:", game_states)
            print("To be even more clear, you must press the buttons on the following coordinates: ")
            print(final_coordinates)
            break
"""