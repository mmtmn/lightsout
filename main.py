# made by Thiago M Nóbrega
# to run this project: python main.py
import os

def main():
    """ this is the main menu function, where the user can choose
        which way to solve the 'lights out' game.
    """
    print("")
    print("Hello and Welcome to this Lights Out Solver Main Menu!")
    print("Made by Thiago M Nóbrega")
    print("")
    print("Options: ")
    print("1. Solve a 3x3 lights out game by states of spaces")
    print("2. Solve a 3x3 lights out game by brute forcing randomly")
    print("3. Solve a 5x5 lights out game by heuristics")
    print("4. Eastern egg")
    print("5. Exit")
    print("")
    print("")
    while True:
        try:
            x = int(input('Your choice: '))
            break
        except:
            print("Invalid option. Please try again.")
        
    if x == 1:
        os.system('cls||clear')
        from stateSpace import StateSpace
        StateSpace()

    elif x == 2:
        os.system('cls||clear')
        from bruteForce import BruteForce
        BruteForce()
        
    elif x == 3:
        os.system('cls||clear')
        from heuristics import HeuristicsResolution
        HeuristicsResolution()
        
    elif x == 4:
        os.system('cls||clear')
        from multiple_lights import eastern_egg
        eastern_egg()
        
    elif x == 5:
        os.system('cls||clear')
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