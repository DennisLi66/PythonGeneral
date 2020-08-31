import random

def numberGuesser():
    while (True):
        print("Please choose an acceptable range:");
        print("[0]: 1 - 10");
        print("[1]: 1 - 100");
        print("[Q]uit or [q]uit");
        chosen = 0;
        guesses = 0;
        won = False;
        while(True):
            rangch = input()
            if (rangch == '0'):
                print("You've chosen 1 - 10.");
                chosen = random.randint(1,10);
                guesses = 3;
                break;
            elif (rangch == '1'):
                print("You've chosen 1 - 100.");
                chosen = random.randint(1,100);
                guesses = 7;
                break;
            elif ((rangch == "q") or (rangch == "Q")):
                return;
            else:
                print("Not a valid option.");
        while (guesses > 0):
            print("Attempts Remaining:" + str(guesses));
            pick = input();
            if (not pick.isdecimal()):
                print("Not a valid number.");
                continue;
            pick = int(pick);
            if (pick == chosen):
                print("You've chosen correctly! The answer was in fact " + str(chosen) + ".")
                won = True;
                break;
            elif (pick < chosen):
                print("Incorrect. The answer is higher than your guess of " + str(pick) + ".")
            elif (pick > chosen):
                print("Incorrect. The answer is lower than you guess of " + str(pick) + ".");
            guesses-= 1;
        if (not won):
            print("You're out of guesses. The answer was " + str(chosen) + ".");
        print("Would you like to play again?");
        print("{Y]es or [y]es");
        print("[N]o or [n]o");
        while (True):
            cont = input();
            if ((cont == "y") or (cont == "Y")):
                continue;
            elif ((cont == "n") or (cont == "N")):
                return;
            else:
                print("That was not a valid choice");
        
        
