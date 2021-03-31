import os

def eastern_egg():
    os.system('clear || cls')
    print("")
    print("To use 2 different lights, choose either option 1 or 2 in the main menu")
    print("This way, you'll be using the 3 by 3 lights out game")
    print("")
    print("now, for each row, choose either 1, 0 or -1")
    print("")
    print("0 = the light is out")
    print("1 = light color 1 is on")
    print("-1 = light color 2 is on")
    print("")
    print("To use a negative number in a row, please input the row's value twice with the negative number.")
    print("")
    def option():
        while True:
            try:
                x = int(input("Press 1 to go back to the Main Menu: "))
                break
            except:
                print("Please press 1 to go back to the Main Menu")
        if x == 1:
            os.system('clear || cls')
            from main import main
            main()
        else:
            option()
    option()