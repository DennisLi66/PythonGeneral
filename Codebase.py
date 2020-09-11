import numberGuesser
import simplePhonebook as simpPBK
import feelingLucky as GoogleSpawn


print("Welcome to Dennis' misc Python codes");
while (True):
    print('Press [0] for the number guesser');
    print('Press [1] for the simple phonebook');
    print('Press [2] for the Google Search Site Spawner');
    print('[Q]uit/[q]uit');
    choice = input();
    if (choice == '0'):
        print("You selected Number Guesser!");
        numberGuesser.numberGuesser();
    elif (choice == '1'):
        print("You selected Simple Phonebook");
        simpPBK.runBook();
    elif (choice == '2'):
        print("You selected Google Search Site Spawner");
        GoogleSpawn.interface();
    elif ((choice == 'Q') or (choice == 'q')):
        break;
    else:
        print("Sorry, that was not a valid option.")
    
    



