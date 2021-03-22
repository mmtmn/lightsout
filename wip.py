def inicialInputs():
        # row 1
        row1 = list(map(int, input("row #1: ").split()))
        if len(row1) != 5:
            while len(row1) != 5:
                row1 = list(map(int, input("row #1: ").split()))
                for x in row1:
                    if x != 0 and x != 1:
                        row1 = list(map(int, input("row #1: ").split()))
        if len(row1) == 5:
            for x in row1:
                if x != 0 and x != 1:
                    row1 = list(map(int, input("row #1: ").split()))
                    
        # row 2
        row2 = list(map(int, input("row #2: ").split()))
        if len(row2) != 5:
            while len(row2) != 5:
                row2 = list(map(int, input("row #2: ").split()))
                for x in row2:
                    if x != 0 and x != 1:
                        row2 = list(map(int, input("row #2: ").split()))
        if len(row2) == 5:
            for x in row2:
                if x != 0 and x != 1:
                    row2 = list(map(int, input("row #2: ").split()))  
        # row 3
        row3 = list(map(int, input("row #3: ").split()))
        if len(row3) != 5:
            while len(row3) != 5:
                row3 = list(map(int, input("row #3: ").split()))
                for x in row3:
                    if x != 0 and x != 1:
                        row3 = list(map(int, input("row #3: ").split()))
        if len(row3) == 5:
            for x in row1:
                if x != 0 and x != 1:
                    row3 = list(map(int, input("row #3: ").split()))  

        # row 4
        row4 = list(map(int, input("row #4: ").split()))
        if len(row4) != 5:
            while len(row4) != 5:
                row4 = list(map(int, input("row #4: ").split()))
                for x in row4:
                    if x != 0 and x != 1:
                        row4 = list(map(int, input("row #4: ").split()))
        if len(row4) == 5:
            for x in row4:
                if x != 0 and x != 1:
                    row4 = list(map(int, input("row #4: ").split()))  

        # row 5
        row5 = list(map(int, input("row #5: ").split()))
        if len(row5) != 5:
            while len(row5) != 5:
                row5 = list(map(int, input("row #5: ").split()))
                for x in row5:
                    if x != 0 and x != 1:
                        row5 = list(map(int, input("row #5: ").split()))
        if len(row5) == 5:
            for x in row5:
                if x != 0 and x != 1:
                    row5 = list(map(int, input("row #5: ").split()))  
        return row1,row2,row3,row4,row5
    inicialInputs()
    allRows = inicialInputs()
