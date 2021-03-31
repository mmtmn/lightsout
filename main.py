# made by Thiago M Nóbrega
# to run this project: python main.py

def main():
    print("")
    print("Hello and Welcome to this Lights Out Solver!")
    print("Made by Thiago M Nóbrega")
    print("")
    print("Options: ")
    print("1. Solve a 3x3 lights out game by states of spaces")
    print("2. Solve a 3x3 lighstout game by random brute force")
    print("3. Solve a 5x5 lights out game by heuristics")
    print("4. exit")
    print("")
    print("")
    while True:
        try:
            x = int(input('Your choice: '))
            break
        except:
            print("Invalid option. Please try again.")
        
    if x == 1:
        from stateSpace import StateSpace
        StateSpace()
        main()
    elif x == 2:
        from bruteForce import BruteForce
        BruteForce()
        main()
    elif x == 3:
        from heuristics import HeuristicsResolution
        HeuristicsResolution()
        main()
    elif x == 4:
        print("")
        print("Thank you so much for your time!")
        print("")
        exit()
    else:
        print("")
        print("Sorry, that was not an option!")
        print("")
        main()

main()
