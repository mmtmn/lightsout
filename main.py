def main():
    print("")
    print("Hello and Welcome to this Lights Out Solver!")
    print("Options: ")
    print("1. Solve a 3x3 lights out game by states of spaces")
    print("2. Solve a 5x5 lights out game by heuristics")
    print("3. exit")
    print("")
    x = int(input("You choice: "))
    if x == 1:
        from Heuristics import lightsOutHeuristicsResolution
        lightsOutHeuristicsResolution()
        main()
    elif x ==2:
        print("Hello")
        main()
    elif x == 3:
        print("")
        print("Thank you so much for your time!")
        print("")
        exit
    else:
        print("")
        print("Sorry, that was not an option!")
        print("")
        main()
main()
